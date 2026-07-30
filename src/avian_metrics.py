"""
Avian breeding outcome metrics and egg-record validation.

Implements derived rates and logical rules from DATA_DICTIONARY.md
(Sunshine BirdWorld avian research repository).

Contact: info@sunshinebirdworld.org · https://www.sunshinebirdworld.org
"""

from __future__ import annotations

from typing import Callable, Iterable, Mapping, Optional, Sequence, Tuple, Union

import numpy as np
import pandas as pd
from scipy import stats

# ---------------------------------------------------------------------------
# Required egg-table columns (DATA_DICTIONARY §6)
# ---------------------------------------------------------------------------
REQUIRED_EGG_COLUMNS: Tuple[str, ...] = (
    "egg_id",
    "clutch_id",
    "pair_id",
    "species_scientific",
    "lay_date",
    "season",
    "incubation_method",
    "fertility_status",
    "embryo_loss_stage",
    "hatch_status",
    "hatch_assistance",
    "chick_status_day7",
    "data_quality_flag",
    "source_record_type",
    "verified_status",
)

ASSESSABLE_FERTILITY = frozenset({"fertile", "infertile"})
FERTILE = "fertile"
INFERTILE = "infertile"
HATCHED = "hatched"
ALIVE = "alive"
DIED = "died"


def wilson_ci(
    successes: int,
    n: int,
    alpha: float = 0.05,
) -> Tuple[float, float, float]:
    """Wilson score confidence interval for a binomial proportion.

    Parameters
    ----------
    successes :
        Number of successes (numerator).
    n :
        Number of trials (denominator).
    alpha :
        Two-sided Type I error rate; default 0.05 for a 95% interval.

    Returns
    -------
    estimate, low, high :
        Point estimate ``successes / n`` and Wilson lower/upper bounds.
        If ``n == 0``, returns ``(nan, nan, nan)``.
    """
    successes = int(successes)
    n = int(n)
    if n < 0 or successes < 0 or successes > n:
        raise ValueError(
            f"Invalid counts: successes={successes}, n={n} "
            "(require 0 <= successes <= n and n >= 0)."
        )
    if n == 0:
        return (float("nan"), float("nan"), float("nan"))

    z = float(stats.norm.ppf(1.0 - alpha / 2.0))
    phat = successes / n
    z2 = z * z
    denom = 1.0 + z2 / n
    centre = phat + z2 / (2.0 * n)
    margin = z * np.sqrt((phat * (1.0 - phat) + z2 / (4.0 * n)) / n)
    low = (centre - margin) / denom
    high = (centre + margin) / denom
    return (float(phat), float(max(0.0, low)), float(min(1.0, high)))


def proportion_table(
    successes: int,
    n: int,
    label: Optional[str] = None,
    alpha: float = 0.05,
) -> pd.Series:
    """Summarise a binomial proportion with Wilson CI.

    Returns a Series with ``n``, ``successes``, ``rate``, ``ci_low``,
    ``ci_high``. Optionally named by ``label``.
    """
    estimate, low, high = wilson_ci(successes, n, alpha=alpha)
    out = pd.Series(
        {
            "n": int(n),
            "successes": int(successes),
            "rate": estimate,
            "ci_low": low,
            "ci_high": high,
        }
    )
    if label is not None:
        out.name = label
    return out


def _eligible(df: pd.DataFrame, quality_ok_only: bool = False) -> pd.DataFrame:
    """Return analysis frame; optionally restrict to ``data_quality_flag == 'ok'``."""
    if quality_ok_only and "data_quality_flag" in df.columns:
        return df.loc[df["data_quality_flag"].astype(str) == "ok"].copy()
    return df.copy()


def fertility_rate(
    df: pd.DataFrame,
    *,
    quality_ok_only: bool = False,
    label: Optional[str] = "fertility_rate",
) -> pd.Series:
    """Fertility rate = F / N_A.

    ``N_A`` = eggs with assessable fertility (``fertile`` or ``infertile``);
    ``F`` = fertile eggs. Eggs with ``unknown`` / ``not_assessed`` fertility
    are excluded from the denominator (DATA_DICTIONARY §13).
    """
    work = _eligible(df, quality_ok_only=quality_ok_only)
    assessable = work["fertility_status"].isin(ASSESSABLE_FERTILITY)
    n_a = int(assessable.sum())
    f = int((work.loc[assessable, "fertility_status"] == FERTILE).sum())
    return proportion_table(f, n_a, label=label)


def overall_hatch_rate(
    df: pd.DataFrame,
    *,
    quality_ok_only: bool = False,
    label: Optional[str] = "overall_hatch_rate",
) -> pd.Series:
    """Overall hatch rate = H / N (live hatches among all eligible eggs)."""
    work = _eligible(df, quality_ok_only=quality_ok_only)
    n = len(work)
    h = int((work["hatch_status"] == HATCHED).sum())
    return proportion_table(h, n, label=label)


def hatchability_of_fertile(
    df: pd.DataFrame,
    *,
    quality_ok_only: bool = False,
    label: Optional[str] = "hatchability_of_fertile",
) -> pd.Series:
    """Hatchability of fertile eggs = H / F."""
    work = _eligible(df, quality_ok_only=quality_ok_only)
    fertile = work["fertility_status"] == FERTILE
    f = int(fertile.sum())
    h = int((work.loc[fertile, "hatch_status"] == HATCHED).sum())
    return proportion_table(h, f, label=label)


def day7_survival(
    df: pd.DataFrame,
    *,
    quality_ok_only: bool = False,
    label: Optional[str] = "day7_survival",
) -> pd.Series:
    """Seven-day survival among known outcomes = S_7 / (S_7 + D_7).

    Only chicks with ``chick_status_day7`` in {``alive``, ``died``} enter
    the denominator (DATA_DICTIONARY §13).
    """
    work = _eligible(df, quality_ok_only=quality_ok_only)
    known = work["chick_status_day7"].isin({ALIVE, DIED})
    s7 = int((work.loc[known, "chick_status_day7"] == ALIVE).sum())
    d7 = int((work.loc[known, "chick_status_day7"] == DIED).sum())
    return proportion_table(s7, s7 + d7, label=label)


def validate_egg_schema(df: pd.DataFrame) -> dict:
    """Check that required egg-table columns are present.

    Returns
    -------
    dict
        ``ok`` (bool), ``missing_columns`` (list), ``extra_info`` (str),
        ``n_rows``, ``n_columns``.
    """
    missing = [c for c in REQUIRED_EGG_COLUMNS if c not in df.columns]
    return {
        "ok": len(missing) == 0,
        "missing_columns": missing,
        "n_rows": int(len(df)),
        "n_columns": int(df.shape[1]),
        "required_columns": list(REQUIRED_EGG_COLUMNS),
        "extra_info": (
            "Schema valid: all required egg columns present."
            if not missing
            else f"Missing required columns: {missing}"
        ),
    }


def check_logical_rules(df: pd.DataFrame) -> pd.DataFrame:
    """Implement the nine logical validation rules from DATA_DICTIONARY §6.

    Returns a DataFrame with one row per rule:
    ``rule_id``, ``description``, ``n_violations``, ``violating_egg_ids``,
    ``passed``.
    """
    work = df.copy()
    if "lay_date" in work.columns:
        work["_lay"] = pd.to_datetime(work["lay_date"], errors="coerce")
    else:
        work["_lay"] = pd.NaT
    if "hatch_date" in work.columns:
        work["_hatch"] = pd.to_datetime(work["hatch_date"], errors="coerce")
    else:
        work["_hatch"] = pd.NaT

    egg_ids = (
        work["egg_id"].astype(str)
        if "egg_id" in work.columns
        else pd.Series([f"row_{i}" for i in range(len(work))])
    )

    rules: list[dict] = []

    # 1. egg_id must be unique
    if "egg_id" in work.columns:
        dup_mask = work["egg_id"].duplicated(keep=False) & work["egg_id"].notna()
        viol = egg_ids.loc[dup_mask].unique().tolist()
    else:
        viol = ["<egg_id column missing>"]
    rules.append(_rule_row(1, "egg_id must be unique", viol))

    # 2. hatch_status = hatched requires fertility_status = fertile
    mask2 = (work["hatch_status"] == HATCHED) & (work["fertility_status"] != FERTILE)
    rules.append(
        _rule_row(
            2,
            "hatch_status=hatched requires fertility_status=fertile",
            egg_ids.loc[mask2].tolist(),
        )
    )

    # 3. hatch_status = hatched requires a hatch_date
    if "hatch_date" in work.columns:
        hatch_date_missing = work["hatch_date"].isna() | (
            work["hatch_date"].astype(str).str.strip() == ""
        )
    else:
        hatch_date_missing = pd.Series(True, index=work.index)
    mask3 = (work["hatch_status"] == HATCHED) & hatch_date_missing
    rules.append(
        _rule_row(
            3,
            "hatch_status=hatched requires a hatch_date",
            egg_ids.loc[mask3].tolist(),
        )
    )

    # 4. hatch_date cannot precede lay_date
    mask4 = work["_hatch"].notna() & work["_lay"].notna() & (work["_hatch"] < work["_lay"])
    rules.append(
        _rule_row(
            4,
            "hatch_date cannot precede lay_date",
            egg_ids.loc[mask4].tolist(),
        )
    )

    # 5. chick_status_day7 is applicable only to hatched eggs
    #    Applicable means not 'not_applicable'; for non-hatched eggs it must be not_applicable
    #    (or blank treated carefully). Violation: non-hatched with a day7 status that is
    #    not 'not_applicable'.
    day7 = work["chick_status_day7"].astype(str)
    mask5 = (work["hatch_status"] != HATCHED) & (
        day7.notna()
        & (day7 != "nan")
        & (day7.str.strip() != "")
        & (day7 != "not_applicable")
    )
    # Also: hatched eggs should not be marked not_applicable (soft consistency)
    # Dictionary: "applicable only to hatched" — so the hard rule is non-hatched ⇒ N/A.
    rules.append(
        _rule_row(
            5,
            "chick_status_day7 is applicable only to hatched eggs",
            egg_ids.loc[mask5].tolist(),
        )
    )

    # 6. embryo_loss_stage is not_applicable for infertile eggs
    mask6 = (work["fertility_status"] == INFERTILE) & (
        work["embryo_loss_stage"].astype(str) != "not_applicable"
    )
    rules.append(
        _rule_row(
            6,
            "embryo_loss_stage is not_applicable for infertile eggs",
            egg_ids.loc[mask6].tolist(),
        )
    )

    # 7. A fertile, non-hatched egg should have a loss stage or unknown
    #    (not 'none' and not 'not_applicable')
    loss = work["embryo_loss_stage"].astype(str)
    mask7 = (
        (work["fertility_status"] == FERTILE)
        & (work["hatch_status"] != HATCHED)
        & ~loss.isin({"early", "middle", "late", "unknown"})
    )
    rules.append(
        _rule_row(
            7,
            "fertile non-hatched egg should have loss stage or unknown",
            egg_ids.loc[mask7].tolist(),
        )
    )

    # 8. initial_weight_g must be positive (species-specific limits not hard-coded)
    if "initial_weight_g" in work.columns:
        w = pd.to_numeric(work["initial_weight_g"], errors="coerce")
        # Only flag non-missing non-positive weights
        mask8 = w.notna() & (w <= 0)
        viol8 = egg_ids.loc[mask8].tolist()
    else:
        viol8 = []
    rules.append(
        _rule_row(
            8,
            "initial_weight_g must be positive when present (species limits external)",
            viol8,
        )
    )

    # 9. exclusion_reason must be present when data_quality_flag = exclude
    if "data_quality_flag" in work.columns:
        is_exclude = work["data_quality_flag"].astype(str) == "exclude"
        if "exclusion_reason" in work.columns:
            er = work["exclusion_reason"]
            reason_missing = er.isna() | (er.astype(str).str.strip() == "") | (
                er.astype(str).str.lower() == "nan"
            )
        else:
            reason_missing = pd.Series(True, index=work.index)
        mask9 = is_exclude & reason_missing
        viol9 = egg_ids.loc[mask9].tolist()
    else:
        viol9 = []
    rules.append(
        _rule_row(
            9,
            "exclusion_reason required when data_quality_flag=exclude",
            viol9,
        )
    )

    return pd.DataFrame(rules)


def _rule_row(rule_id: int, description: str, violating_ids: Sequence) -> dict:
    ids = list(violating_ids)
    return {
        "rule_id": rule_id,
        "description": description,
        "n_violations": len(ids),
        "violating_egg_ids": ids,
        "passed": len(ids) == 0,
    }


def duplicate_report(df: pd.DataFrame, id_col: str = "egg_id") -> dict:
    """Report duplicate identifiers in ``id_col``.

    Returns counts and the list of duplicated ID values.
    """
    if id_col not in df.columns:
        return {
            "id_col": id_col,
            "n_rows": int(len(df)),
            "n_unique": 0,
            "n_duplicate_rows": 0,
            "n_duplicated_ids": 0,
            "duplicated_ids": [],
            "ok": False,
            "message": f"Column '{id_col}' not found.",
        }
    series = df[id_col]
    duplicated_ids = series[series.duplicated(keep=False) & series.notna()].unique().tolist()
    n_dup_rows = int(series.duplicated(keep=False).sum())
    return {
        "id_col": id_col,
        "n_rows": int(len(df)),
        "n_unique": int(series.nunique(dropna=True)),
        "n_duplicate_rows": n_dup_rows,
        "n_duplicated_ids": len(duplicated_ids),
        "duplicated_ids": duplicated_ids,
        "ok": n_dup_rows == 0,
        "message": (
            "No duplicate egg_id values."
            if n_dup_rows == 0
            else f"{len(duplicated_ids)} duplicated id(s) across {n_dup_rows} rows."
        ),
    }


def missingness_report(df: pd.DataFrame) -> pd.DataFrame:
    """Per-column missingness counts and rates.

    Empty strings are treated as missing in addition to NaN.
    """
    rows = []
    n = len(df)
    for col in df.columns:
        s = df[col]
        if pd.api.types.is_string_dtype(s) or s.dtype == object:
            miss = s.isna() | (s.astype(str).str.strip() == "") | (s.astype(str) == "nan")
        else:
            miss = s.isna()
        n_miss = int(miss.sum())
        rows.append(
            {
                "column": col,
                "n_missing": n_miss,
                "n_present": n - n_miss,
                "missing_rate": (n_miss / n) if n else float("nan"),
            }
        )
    return pd.DataFrame(rows).sort_values("n_missing", ascending=False).reset_index(drop=True)


def stratified_proportion(
    df: pd.DataFrame,
    group_col: str,
    outcome_fn: Callable[[pd.DataFrame], pd.Series],
) -> pd.DataFrame:
    """Apply an outcome metric function within strata of ``group_col``.

    ``outcome_fn`` should accept a DataFrame slice and return a Series from
    :func:`proportion_table` (keys: n, successes, rate, ci_low, ci_high).

    Returns a DataFrame with the grouping column plus proportion columns.
    """
    if group_col not in df.columns:
        raise KeyError(f"Grouping column '{group_col}' not found.")

    records = []
    for key, group in df.groupby(group_col, dropna=False):
        summary = outcome_fn(group)
        rec = {group_col: key}
        rec.update(summary.to_dict())
        records.append(rec)
    out = pd.DataFrame(records)
    if not out.empty and "rate" in out.columns:
        out = out.sort_values(group_col, kind="mergesort").reset_index(drop=True)
    return out


def core_metrics_summary(
    df: pd.DataFrame,
    *,
    quality_ok_only: bool = False,
) -> pd.DataFrame:
    """Compute the four core derived metrics as a single tidy table."""
    metrics = [
        fertility_rate(df, quality_ok_only=quality_ok_only),
        overall_hatch_rate(df, quality_ok_only=quality_ok_only),
        hatchability_of_fertile(df, quality_ok_only=quality_ok_only),
        day7_survival(df, quality_ok_only=quality_ok_only),
    ]
    rows = []
    for s in metrics:
        row = s.to_dict()
        row["metric"] = s.name
        rows.append(row)
    return pd.DataFrame(rows)[
        ["metric", "n", "successes", "rate", "ci_low", "ci_high"]
    ]


def embryo_loss_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Summarise embryo-loss stages among fertile, non-hatched eggs."""
    fertile_unhatched = df[
        (df["fertility_status"] == FERTILE) & (df["hatch_status"] != HATCHED)
    ].copy()
    n = len(fertile_unhatched)
    if n == 0:
        return pd.DataFrame(
            columns=["embryo_loss_stage", "n", "proportion_of_fertile_unhatched"]
        )
    counts = (
        fertile_unhatched["embryo_loss_stage"]
        .fillna("missing")
        .value_counts(dropna=False)
        .rename_axis("embryo_loss_stage")
        .reset_index(name="n")
    )
    counts["proportion_of_fertile_unhatched"] = counts["n"] / n
    counts["n_fertile_unhatched"] = n
    return counts
