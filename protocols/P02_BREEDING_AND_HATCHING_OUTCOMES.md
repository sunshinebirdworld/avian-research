# P02 — Breeding and Hatching Outcomes

| Metadata | Value |
|---|---|
| **Protocol ID** | P02 |
| **Title** | Breeding and Hatching Outcomes |
| **Version** | v0.1.0 |
| **Effective date** | 2026-07-30 |
| **Status** | Active |
| **Parent documents** | [`RESEARCH_SCOPE.md`](../RESEARCH_SCOPE.md) Aims 1–2; [`DATA_DICTIONARY.md`](../DATA_DICTIONARY.md) clutch and egg tables |
| **Licence** | Documentation: CC BY 4.0; code: Apache-2.0 |

## 1. Purpose

This protocol standardises definitions, denominators, inclusion and exclusion rules, stratification, and reporting requirements for fertility, embryo loss, hatch, hatch assistance, and early chick survival in managed avicultural populations at Sunshine BirdWorld. It links operational recording practice to the egg and hatch table fields used by reproducible analyses.

## 2. Scope

### In scope

- Outcome definitions for eggs and hatched chicks through day 7 (and optional later survival endpoints when collected).
- Denominator construction for fertility rate, overall hatch rate, hatchability of fertile eggs, assistance rate, and day-7 survival.
- Inclusion and exclusion rules; duplicate resolution.
- Stratification by species, season, and incubation method.
- Reporting requirements for manuscripts, notebooks, and aggregate tables.
- Linkage to dictionary fields on the egg/hatch table.

### Out of scope

- Commercial production targets or sale metrics.
- Causal claims from uncontrolled observational contrasts.
- Publication of exact enclosure maps or parental identity beyond pseudonymous `pair_id` / `bird_id`.
- Treating synthetic demonstration results as Sunshine BirdWorld performance statistics.

> **Synthetic data notice.** The repository notebook and example CSV use synthetic egg records to demonstrate calculations. Those percentages are not real Sunshine BirdWorld hatch or survival results.

## 3. Core outcome definitions

Apply definitions consistently within a frozen analysis version. If candling practice or breakout policy changes, bump the protocol or analysis-plan version and document the migration effect on historical rates.

### 3.1 Fertility (`fertility_status`)

| Value | Definition |
|---|---|
| `fertile` | Evidence of embryonic development under the stated `fertility_basis` (candling, breakout examination, imaging, hatch, or combined). |
| `infertile` | Assessed with an adequate method and no evidence of development. |
| `unknown` | Assessment attempted or partially recorded but classification remains unresolved. |
| `not_assessed` | No fertility determination performed (distinct from unknown). |

**Rules**

- A live hatch implies `fertile`.
- Do not code infertile merely because an egg failed to hatch; failure to hatch in a fertile egg is embryo loss or other hatch failure.
- Record `fertility_basis` whenever feasible.
- Eggs with `not_assessed` or `unknown` fertility are excluded from the fertility-rate denominator \(N_A\) but counted in overall eligibility audits.

### 3.2 Embryo loss stage (`embryo_loss_stage`)

Used when a fertile egg does not produce a live hatch.

| Value | Operational meaning |
|---|---|
| `none` | No embryo loss (typically reserved for hatched eggs). |
| `early` | Death or developmental arrest in the early embryonic period as defined for the species’ incubation length in the analysis plan (default working rule: first third of expected incubation, unless species SOP states otherwise). |
| `middle` | Arrest in the middle third of expected incubation. |
| `late` | Arrest in the final third, including dead-in-shell near term without live hatch. |
| `unknown` | Fertile non-hatch without reliable staging. |
| `not_applicable` | Required for infertile eggs and for eggs not in the fertile non-hatch pathway. |

Staging must cite whether classification used candling chronology, breakout anatomy, or both. Mixed evidence is coded with the best-supported stage and a data-quality flag if conflict remains.

### 3.3 Hatch (`hatch_status`)

| Value | Definition |
|---|---|
| `hatched` | Live chick fully or substantially emerged and alive at the standardised hatch observation under project rules; `hatch_date` required. |
| `not_hatched` | No live hatch. |
| `unknown` | Hatch outcome cannot be resolved from source records. |

Internal pipping alone without a live hatched chick does not satisfy `hatched`. Malposition and hatch abnormality, when recorded, are documented as companion descriptors in restricted notes or future controlled fields; they do not replace `hatch_status`.

### 3.4 Hatch assistance (`hatch_assistance`)

| Value | Definition |
|---|---|
| `none` | No physical assistance documented. |
| `partial` | Limited assistance (for example membrane takedown or positional aid) with substantial unaided progress. |
| `full` | Extensive assistance without which hatch would not have completed under the recorded clinical judgement. |
| `unknown` | Assistance status not recoverable. |
| `not_applicable` | Egg did not enter a hatch attempt pathway (for example early infertile removal per SOP). |

Assistance decisions are clinical/husbandry judgements and are not retrospectively invented for analysis convenience. Assisted hatches remain `hatched` if the live-hatch definition is met; assistance is analysed as a separate rate.

### 3.5 Day-7 survival (`chick_status_day7`)

Applicable only when `hatch_status = hatched`.

| Value | Definition |
|---|---|
| `alive` | Chick alive at the end of day 7 after `hatch_date` (seven completed 24-hour periods). |
| `died` | Confirmed death on or before day 7. |
| `lost_to_followup` | Hatched chick with unknown status at day 7. |
| `unknown` | Records insufficient to classify. |
| `not_applicable` | Non-hatched eggs. |

Optional later endpoints (day 30, weaning) follow the same logic when those fields are collected prospectively; they are not required for P02 minimum reporting.

## 4. Denominators and primary metrics

Let:

- \(N\) = eligible eggs after inclusion/exclusion for the analysis population;
- \(N_A\) = eggs with assessable fertility (`fertile` or `infertile`);
- \(F\) = fertile eggs;
- \(H\) = live hatches;
- \(A\) = hatches with `hatch_assistance` in {`partial`, `full`} among hatched eggs with known assistance;
- \(S_7\) = chicks alive at day 7;
- \(D_7\) = chicks dead by day 7 with known status.

| Metric | Formula | Notes |
|---|---|---|
| Fertility rate | \(F / N_A\) | Exclude `unknown` and `not_assessed` from denominator. |
| Overall hatch rate | \(H / N\) | All eligible eggs. |
| Hatchability of fertile eggs | \(H / F\) | Primary incubation-performance metric among fertiles. |
| Assistance rate | \(A / H_{\mathrm{known\ assistance}}\) | State if `unknown` assistance is excluded. |
| Day-7 survival (known outcomes) | \(S_7 / (S_7 + D_7)\) | Exclude `lost_to_followup` / `unknown` from this denominator; report their counts separately. |

Every published percentage must print numerator and denominator. A percentage without its denominator is incomplete.

## 5. Inclusion criteria

Include an egg record when all of the following hold:

1. `egg_id` is unique and linkable to `clutch_id` and `pair_id` under public pseudonymous IDs.
2. `species_scientific` is present and taxonomically acceptable for the analysis version.
3. `lay_date` is present with usable precision for the planned time window.
4. Outcome fields required for the selected metric are populated or explicitly coded as unknown/not assessed.
5. `data_quality_flag` is `ok` or `review` (review records need resolution before confirmatory analysis).
6. Inclusion is lawful and consistent with P01 release rules for the intended output tier.

## 6. Exclusion criteria

Exclude (and count) when:

- identity or clutch linkage cannot be resolved;
- duplicate `egg_id` or duplicate physical egg after adjudication;
- internally impossible dates (`hatch_date` before `lay_date`);
- `data_quality_flag = exclude` with coded `exclusion_reason`;
- egg outside the prespecified population (species, season window, or study cohort);
- source record unreliable and not independently verifiable;
- public release would create disproportionate privacy, welfare, or security risk (handle under P01 rather than silently dropping from internal audits).

Do not exclude solely because an outcome is unfavourable.

## 7. Stratification

Prespecify strata before looking at endpoint contrasts whenever the analysis is confirmatory.

### Required candidate strata

- `species_scientific` (do not pool biologically dissimilar species without justification);
- `season` / `season_label` (project-defined breeding periods fixed in the analysis plan);
- `incubation_method` (`parental`, `artificial`, `mixed`, `unknown`).

### Additional strata when powered and scientifically motivated

- clutch size band;
- parental versus mixed strategies at clutch level (`incubation_strategy`);
- assist versus unassisted among hatches;
- lay-order within clutch if reliably recorded in a future field extension.

Small strata must show exact counts and Wilson intervals; avoid species-level claims when \(n\) is too small to support them.

## 8. Procedure — recording to analysis

1. **At lay:** assign `egg_id`, link `clutch_id` / `pair_id`, record `lay_date`, species, season, initial weight if measured.
2. **During incubation:** record incubation method; document candling schedule in the source layer; update fertility and embryo-loss fields when evidence accrues.
3. **At hatch window:** set `hatch_status`, `hatch_date`, `hatch_assistance`; create `chick_id` when a stable identity exists.
4. **Through day 7:** update `chick_status_day7`.
5. **Verification:** set `verified_status` (`unverified` / `single_checked` / `double_checked`) and `source_record_type`.
6. **Freeze:** under P06, freeze the egg table version; run logical validation rules from the data dictionary.
7. **Analyse:** compute metrics with stated denominators; stratify; report missingness and exclusions.
8. **Release:** apply P01 before any public table leaves the institution.

## 9. Logical validation rules (egg table)

Enforce dictionary rules:

1. Unique `egg_id`.
2. `hatch_status = hatched` ⇒ `fertility_status = fertile`.
3. `hatch_status = hatched` ⇒ `hatch_date` present.
4. `hatch_date` ≥ `lay_date`.
5. `chick_status_day7` applicable only if hatched.
6. `embryo_loss_stage = not_applicable` for infertile eggs.
7. Fertile + not hatched ⇒ loss stage in {`early`, `middle`, `late`, `unknown`}.
8. `initial_weight_g` positive and species-plausible.
9. `exclusion_reason` present when `data_quality_flag = exclude`.

## 10. Reporting requirements

Any public or manuscript-facing breeding-outcomes report must include:

- protocol and data-dictionary versions;
- data cutoff and analysis population;
- flow counts: reviewed → eligible → included by metric;
- numerators and denominators for each metric;
- Wilson (or other exact) 95% confidence intervals for proportions (see P06);
- stratification tables or a justification for pooling;
- missingness for critical fields;
- clustering caveat (eggs within clutches/pairs are not independent);
- limitations and non-causal language for observational contrasts;
- explicit statement if any displayed data are synthetic.

## 11. Required field references

Egg and hatch table fields: `egg_id`, `clutch_id`, `pair_id`, `species_scientific`, `species_common`, `lay_date`, `season`, `incubation_method`, `initial_weight_g`, `fertility_status`, `fertility_basis`, `embryo_loss_stage`, `hatch_status`, `hatch_date`, `hatch_assistance`, `chick_id`, `chick_status_day7`, `exclusion_reason`, `data_quality_flag`, `source_record_type`, `verified_status`.

Related clutch fields: `clutch_start_date`, `clutch_size_total`, `season_label`, `incubation_strategy`.

Derived metrics: fertility rate, overall hatch rate, hatchability of fertile eggs, seven-day survival among known outcomes.

## 12. Quality checks

- Completeness ≥95% for critical outcome fields before confirmatory analysis.
- Duplicate and date-logic audit.
- Cross-check that assistance and day-7 fields are not filled for non-hatched eggs.
- Species-specific weight plausibility against a validation table.
- Independent second check for manuscript primary endpoints.

## 13. Responsible roles

| Role | Responsibilities |
|---|---|
| Breeding records steward | Day-to-day egg/clutch entry and source provenance |
| Avian veterinarian / nursery lead | Assistance classification; welfare-linked hatch decisions; review of neonatal deaths |
| Analyst | Denominators, strata, intervals, clustering notes |
| Data steward | P01 release review of outcome tables |
| Project leads | Approval of institutional (non-synthetic) public breeding summaries |

## 14. Limitations

- Candling and breakout staging have imperfect sensitivity and specificity; misclassified fertility biases hatchability of fertiles.
- Assistance practices vary with staffing and species; rates are not automatically comparable across facilities.
- Day-7 survival ignores later juvenile mortality.
- Seasonal labels are project-defined and may not match meteorological seasons elsewhere.
- Single-facility estimates do not represent global aviculture.

## 15. Change control

| Version | Date | Summary |
|---|---|---|
| v0.1.0 | 2026-07-30 | Initial public protocol with dictionary-aligned egg outcome definitions |

Changes to fertility, loss-stage boundaries, hatch, assistance, or survival definitions require a version bump, expected effect on historical rates, and a migration rule. Silently changing definitions is not permitted.
