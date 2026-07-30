# P06 — Reproducible Analysis

| Metadata | Value |
|---|---|
| **Protocol ID** | P06 |
| **Title** | Reproducible Analysis |
| **Version** | v0.1.0 |
| **Effective date** | 2026-07-30 |
| **Status** | Active |
| **Parent documents** | [`RESEARCH_SCOPE.md`](../RESEARCH_SCOPE.md) Sections 10–11, 14; [`DATA_DICTIONARY.md`](../DATA_DICTIONARY.md); demonstration notebook under `notebooks/` |
| **Licence** | Documentation: CC BY 4.0; code: Apache-2.0 |

## 1. Purpose

This protocol defines how Sunshine BirdWorld freezes analysis datasets, executes notebooks, versions software, estimates proportions with appropriate uncertainty, respects clustering, conducts sensitivity analyses, archives outputs, and labels synthetic versus real data. The goal is that a competent reviewer can regenerate tables and figures from a stated commit and data freeze—or clearly see why regeneration is limited.

## 2. Scope

### In scope

- Analysis dataset freeze and cutoff rules.
- Clean-environment notebook execution.
- Software and dependency versioning.
- Wilson confidence intervals for proportions (and related small-sample practice).
- Clustering and independence caveats.
- Prespecified sensitivity analyses.
- Output archiving and provenance.
- Mandatory synthetic versus real labelling.

### Out of scope

- Treating p-values alone as sufficient evidence.
- Auto-accepting AI-generated statistical claims without human review.
- Presenting synthetic notebook results as Sunshine BirdWorld institutional findings.

> **Synthetic data notice.** `data/example_breeding_events.csv` and outputs from `notebooks/01_breeding_outcomes_analysis.ipynb` are synthetic demonstration artefacts. They prove pipeline executability. They are not real Sunshine BirdWorld breeding results and must not be cited as such.

## 3. Analysis freeze process

1. **Declare the question.** Unit of analysis, primary endpoints, denominators, strata, inclusion/exclusion (protocols P02–P05 as applicable).
2. **Set data cutoff.** Record the cutoff date/time; exclude records accruing after cutoff from the primary freeze.
3. **Extract.** Pull from the authoritative internal store into a versioned analysis table set (`data_version`).
4. **Validate.** Run dictionary logical rules, duplicate checks, and missingness reports. Target ≥95% completeness on critical fields unless studying missingness.
5. **De-identify for the intended tier.** Apply P01 before any freeze copy leaves the controlled environment.
6. **Freeze.** Write immutable freeze artefacts (for example `parquet`/`csv` + checksum + freeze manifest). Do not edit freeze files in place; issue `data_version` increments instead.
7. **Register the analysis plan pointer.** Link protocol versions, dictionary version, git commit (when code is used), and freeze ID.
8. **Execute.** Run notebooks from a clean environment (Section 4).
9. **Review.** Domain and statistical review before public claims.
10. **Archive.** Store outputs and environment metadata (Section 9).

Post-freeze corrections follow P01: correction note, new version, re-execution, and visible change log—never silent mutation of a tagged freeze.

## 4. Notebook execution

### Clean-run rules

- Prefer a fresh virtual environment created from `requirements.txt` (or a locked equivalent when introduced).
- Record Python version and package versions in the notebook or an adjacent `environment.json` / conda-lock style file.
- Run top-to-bottom without relying on leftover interactive state.
- Paths must work from repository root or documented `notebooks/` working directory (demonstration notebook supports both patterns).
- Write figures and tables only under `outputs/` or a freeze-specific output folder listed in the manifest.
- Seed any stochastic routine and document the seed; prefer deterministic methods for primary tables.

### Failure handling

If a clean run fails, fix code or environment definitions; do not patch results by hand in exported CSV files. Hand-edited “results” are not reproducible outputs.

## 5. Software versioning

Minimum archived record for each public analysis:

| Item | Example content |
|---|---|
| Repository commit | Git SHA of analysis code |
| Protocol versions | P02 v0.1.0, P06 v0.1.0, dictionary date/version |
| Data freeze ID | `data_version` + checksum |
| Language | Python 3.x exact version |
| Core packages | pandas, numpy, scipy/statsmodels (as used), jupyter — with versions |
| OS note | darwin/linux as run, when material |

Code is licensed Apache-2.0; analysis documentation and narrative methods remain CC BY 4.0. Third-party packages keep their upstream licences.

## 6. Wilson confidence intervals for proportions

For primary proportion endpoints (fertility rate, hatchability of fertiles, day-7 survival among known outcomes, assay positivity in a defined denominator), report **Wilson score 95% confidence intervals** (or another exact/interval method justified in the analysis plan) especially when \(n\) is small.

### Reporting rules

- Always print \(x / n\) alongside the percentage and interval.
- Do not report only a point estimate for confirmatory proportion claims.
- Use two-sided 95% intervals unless a different alpha is prespecified.
- Implementation should live in reusable code (for example `src/avian_metrics.py`) rather than one-off opaque spreadsheet cells.
- When counts are zero or \(n\) is extremely small, still report Wilson (or exact) intervals and avoid over-precise prose.

Complementary measures (risk differences, odds ratios) require their own interval methods and must respect clustering (Section 7).

## 7. Clustering and independence caveats

Eggs from the same clutch, chicks from the same pair, repeated clinical episodes in the same bird, and repeated samples from the same individual are **not** automatically independent.

### Required practice

- State the unit of analysis before modelling.
- For descriptive proportions at egg level, disclose clutch/pair clustering as a limitation even if the primary table remains egg-denominated.
- When estimating associations, prefer methods that account for clustering (for example cluster-robust variance, mixed models, or clutch-level summaries) when sample structure requires it.
- Do not treat repeated measures as independent replicates of “new birds.”
- Avoid species-pooled claims when clusters and biology differ.

Silence about clustering is a protocol deviation for confirmatory manuscripts.

## 8. Sensitivity analyses

Prespecify at least the sensitivity checks that could reasonably change interpretation:

1. **Inclusion boundary:** include versus exclude `data_quality_flag = review` records after adjudication rules.
2. **Fertility uncertainty:** re-estimate hatchability after excluding `fertility_basis = unknown`.
3. **Assistance:** hatchability and day-7 survival among unassisted hatches only.
4. **Loss to follow-up:** day-7 survival under alternative handling of `lost_to_followup` (exclude versus worst-case/best-case bounds when scientifically justified).
5. **Species restriction:** primary species-stratified estimates versus any cautious pooled estimate.
6. **Environmental exposure definition:** alternate excursion thresholds when P05 features are used.
7. **Date precision:** exclude estimated lay/hatch dates when precision fields indicate coarseness.

Exploratory analyses are allowed but must be labelled exploratory and separated from confirmatory claims (Research Scope Section 10).

## 9. Output archiving

For each freeze execution, archive:

- result tables (CSV or equivalent) with column definitions;
- figures with stable filenames;
- notebook HTML or executed IPYNB when feasible;
- missingness and validation reports;
- software version record;
- short interpretation note distinguishing observation from inference;
- checksums or git-annex/LFS pointers as used by the project.

Public repository `outputs/` may hold demonstration artefacts; institutional real-data archives may remain Tier B/C with manifests only in public view.

## 10. Synthetic versus real data labelling

### Mandatory labels

| Artefact type | Required labelling |
|---|---|
| Synthetic CSV / demo tables | Filename or header README states `synthetic`; table caption states not SBW results |
| Notebooks on synthetic data | Opening markdown cell states synthetic status and non-claim |
| Real institutional analysis | Explicit `real_institutional_data` (or equivalent) in manifest; never use synthetic filenames |
| Mixed documents | Separate sections; no combined averages that blend synthetic and real |

### Non-claims (must remain true)

- Synthetic demonstration datasets are not real-world evidence.
- Successful execution of the demo notebook does not validate any particular Sunshine BirdWorld performance statistic.
- AI-assisted drafting does not replace statistical or veterinary review.

## 11. Procedure — end-to-end checklist

- [ ] Question, unit, endpoints, and denominators written down.
- [ ] Cutoff and freeze ID assigned; checksum recorded.
- [ ] Validation and missingness reports filed.
- [ ] P01 tier checklist completed for any external share.
- [ ] Clean environment run succeeded top-to-bottom.
- [ ] Wilson (or justified alternative) intervals reported with \(x/n\).
- [ ] Clustering caveats stated.
- [ ] Sensitivity analyses run and summarised.
- [ ] Synthetic/real labelling verified in every public artefact.
- [ ] Domain + statistical review completed for confirmatory claims.
- [ ] Contact for corrections: `info@sunshinebirdworld.org`.

## 12. Required field references

Depends on workstream; at minimum provenance fields (`data_version`, `verification_status`, `release_status`) plus endpoint fields from P02–P05. Breeding demo metrics use egg-table fields and derived rates in dictionary Section 13.

## 13. Quality checks

- Re-run produces byte-stable or numerically stable primary tables within documented tolerance.
- No unexplained row loss between validation report and final \(n\).
- Intervals present for primary proportions.
- Outputs path and freeze ID embedded in export metadata or filenames.
- Licence headers respected (Apache-2.0 code; CC BY 4.0 docs).

## 14. Responsible roles

| Role | Responsibilities |
|---|---|
| Analyst / statistician | Freeze execution, intervals, clustering methods, sensitivity set |
| Data steward | Freeze integrity, de-identification, checksums |
| Domain reviewer (breeding lead, avian veterinarian, as relevant) | Endpoint interpretation, welfare-sensitive wording |
| Project leads (Dr. Debashis Banerjee; Dr. Anindita Banerjee) | Approval of public institutional analyses; correction escalation |
| External statistical reviewer (when used) | Independent check of confirmatory inference |

## 15. Limitations

- Reproducibility of public demos does not guarantee that private institutional pipelines are identically configured.
- Wilson intervals address binomial uncertainty, not bias from missing data or selection.
- Cluster-robust methods need enough clusters to be trustworthy.
- Small rare-species samples will remain descriptive despite perfect computational reproducibility.
- AI tools may accelerate coding but can introduce subtle analytic errors if unchecked.

## 16. Change control

| Version | Date | Summary |
|---|---|---|
| v0.1.0 | 2026-07-30 | Initial reproducible analysis protocol (freeze, Wilson CIs, clustering, synthetic labelling) |

Changes to default interval methods, freeze rules, or labelling requirements require a version bump and note on effects for in-flight manuscripts. Silently changing definitions is not permitted.
