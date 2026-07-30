# P04 — Avian Bornavirus Surveillance (Research Governance)

| Metadata | Value |
|---|---|
| **Protocol ID** | P04 |
| **Title** | Avian Bornavirus Surveillance — Research Governance and Evidence Analysis |
| **Version** | v0.1.0 |
| **Effective date** | 2026-07-30 |
| **Status** | Active |
| **Parent documents** | [`RESEARCH_SCOPE.md`](../RESEARCH_SCOPE.md) Aims 4–5; [`DATA_DICTIONARY.md`](../DATA_DICTIONARY.md) diagnostic sample and clinical event tables |
| **Licence** | Documentation: CC BY 4.0; code: Apache-2.0 |

## 1. Purpose

This protocol sets **high-level research governance** for Sunshine BirdWorld work on avian bornavirus (ABV) evidence relevant to proventricular dilatation disease (PDD) and related clinical phenotypes. It standardises case definitions, sampling metadata, harmonised result categories, repeat-testing logic, and DIVA-oriented research questions at the **evidence-analysis** level.

It exists so that surveillance outputs distinguish infection-marker evidence, clinical disease, exposure classification, inconclusive findings, and untested assumptions—without publishing methods that exceed an appropriate open scientific risk boundary.

## 2. Explicit biosafety boundary (mandatory)

### This repository and protocol MUST NOT include

- pathogen culture or propagation procedures;
- optimisation of growth conditions for bornaviruses or any pathogen;
- genetic modification, reverse genetics, or gain-of-function methods;
- instructions intended to increase pathogenicity, host range, immune evasion, environmental persistence, or transmission;
- operational laboratory protocols that would enable replication of high-risk virological work from the public text alone.

### Authorised laboratory work

Any wet-laboratory testing, assay development, or related experimental work must be performed only by qualified and authorised collaborators under applicable biosafety, veterinary, animal-welfare, and regulatory controls. Public materials here are limited to metadata standards, epidemiological definitions, analysis logic, and research questions.

Readers must not interpret this protocol as authorising sample collection, invasive procedures, or laboratory pathogen work without those separate controls.

## 3. Scope

### In scope

- Research case definitions (clinical, laboratory-marker, and combined classifications).
- Minimum sampling and assay metadata for harmonised analysis.
- Result categories and quality-control interpretation.
- Repeat-testing and serial-sample logic.
- Concordance, phenotype association, and DIVA-oriented **evidence questions**.
- Public reporting boundaries for surveillance aggregates.

### Out of scope

- Stepwise laboratory SOPs for virus handling.
- Treatment algorithms presented as unsupervised medical advice.
- Claiming that a single assay result equals clinical PDD.
- Citing synthetic demonstration assay tables as Sunshine BirdWorld surveillance prevalence.

> **Synthetic data notice.** If synthetic diagnostic rows appear in demos, they are schema fixtures only—not ABV prevalence or DIVA study results from Sunshine BirdWorld.

## 4. Case definitions (analysis-level)

Definitions below are for research classification. Veterinary clinical care may use additional judgement not fully captured in structured fields.

### 4.1 Clinical phenotype — PDD-compatible illness

An episode may be labelled **PDD-compatible clinical phenotype** when a veterinary-reviewed clinical event documents a compatible sign cluster (for example progressive gastrointestinal dysfunction with undigested faeces, crop stasis, weight loss, and/or compatible neurological signs) after reasonable exclusion of obvious alternative causes available in that setting.

Coded via clinical event fields (`signs_controlled`, diagnoses, `diagnostic_certainty`, `veterinary_review_status = reviewed` for confirmatory analyses).

### 4.2 Laboratory-marker classifications

Using diagnostic sample rows with `target_name` documenting the ABV-related target (antigen, nucleic acid, antibody, or other validated marker as reported by the testing laboratory):

| Research class | Rule sketch |
|---|---|
| Marker-positive | `result_category = positive` AND `qc_status = passed` (or laboratory-equivalent documented) |
| Marker-negative | `result_category = negative` AND QC acceptable |
| Inconclusive | `result_category = inconclusive` or conflicting serial evidence pending adjudication |
| Invalid | `result_category = invalid` or `qc_status = failed` |
| Not tested | No sample / `not_tested` |

Assay method and laboratory interpretation level (`interpretation_status`) must travel with the class. Cycle thresholds or titres, when present, are stored in assay-specific fields and not treated as universal cut-points across platforms without documented validation.

### 4.3 Combined evidence grades (example framework)

Prespecify in each analysis plan; illustrative grades:

| Grade | Clinical phenotype | Marker evidence |
|---|---|---|
| A | Present (reviewed) | Positive (QC passed) |
| B | Present (reviewed) | Negative / not tested |
| C | Absent / other illness | Positive |
| D | Absent | Negative |
| E | Any | Inconclusive / invalid only |

These grades support concordance tables; they are not statutory disease definitions.

## 5. Sampling metadata requirements

Each ABV-related specimen row must populate dictionary diagnostic fields, including:

- `sample_id`, `bird_id` (when individual-linked), optional `clinical_event_id`;
- `collection_datetime`, `sample_type`, `collection_context` (`clinical`, `routine_surveillance`, `contact_investigation`, `research`, `post_mortem`);
- `target_name`, `assay_method` (method and version), `laboratory_id` (pseudonymous);
- `result_category`, optional `result_value` / `result_unit` / `ct_value`, `reference_interval`;
- `qc_status`, `report_date`, `interpretation_status`;
- `repeat_sample_group_id` when part of a serial testing plan.

Public releases follow P01: no exact locations, no staff identities, and no unnecessary transfer detail. Rare-species longitudinal marker trajectories default to Tier B unless aggregated.

## 6. Result categories and interpretation discipline

1. Harmonise laboratory language into `positive` / `negative` / `inconclusive` / `invalid` / `not_tested` before cross-platform pooling.
2. Failures of QC are `invalid` or excluded from concordance numerators with counts reported.
3. Distinguish:
   - **infection-marker evidence** (assay);
   - **clinical disease** (phenotype);
   - **exposure classification** (epidemiological contact rules defined in the analysis plan);
   - **untested assumptions** (missing samples).
4. Do not pool dissimilar assays without a documented comparability rationale.
5. Pathology or imaging findings supportive of PDD, when available, are linked as separate evidence and not silently equated to a serology or PCR row.

## 7. Repeat testing logic

### Purposes of repeats

- Confirm an unexpected positive or negative in a high-stakes clinical context.
- Assess persistence, conversion, or reversion of markers over time.
- Evaluate pre/post events defined in an analysis plan (for example after movement or clinical recovery)—without implying unvalidated interventions in the public protocol.

### Operational rules for analysis

1. Link serial samples with `repeat_sample_group_id` and ordered `collection_datetime`.
2. Prespecify the primary sample for prevalence snapshots (for example first valid test in window versus most recent).
3. Concordance metrics must state whether they compare paired assays of the same modality, different modalities, or clinical grade versus marker grade.
4. Conversion/reversion definitions require two valid tests separated by a minimum interval stated in the analysis plan.
5. Invalid tests do not count as conversions.
6. Repeat intensity may correlate with clinical suspicion (selection bias); report testing probability by phenotype where possible.

## 8. DIVA-oriented research questions (evidence-analysis level)

DIVA (“differentiating infected from vaccinated animals”) concepts in avian bornavirus research are treated here as **questions for evidence design**, not as product-development or pathogen-manipulation instructions.

Illustrative analysis questions suitable for collaborative protocols:

1. Which combinations of antibody, antigen, and nucleic-acid markers best separate birds with clinical PDD-compatible phenotypes from clinically well birds in this managed population?
2. What is the concordance between marker classes when measured within a defined time window?
3. How stable are marker patterns on repeat testing among clinically recovered versus chronically affected birds?
4. Which candidate outcome measures (clinical severity trajectory, weight trend, marker conversion, survival) are sufficiently complete and unbiased for future controlled collaborative studies?
5. Where would a future DIVA-capable immunisation strategy—if developed elsewhere under proper authorisations—need measurement endpoints that this centre can collect observationally (marker panels, phenotype grades, adverse-event capture)?

Questions about vaccine construction, challenge models, or immune-evasion engineering are **out of scope** for this public protocol.

## 9. Reporting requirements for surveillance outputs

- Case definition versions and vocabulary versions.
- Assay methods and laboratories (pseudonymous) with QC summary.
- Counts by result category and evidence grade; denominators for each claim.
- Selection pathway (clinical testing versus routine surveillance).
- Repeat-test rules and concordance tables.
- Limitations: assay performance uncertainty, missingness, species heterogeneity, non-causal language.
- Biosafety boundary statement restated in manuscripts that cite this protocol.
- Synthetic versus real labelling when demo data are shown.

## 10. Procedure — governance workflow

1. Confirm that the proposed analysis needs only metadata and results already generated under authorised laboratory arrangements.
2. Register the analysis plan: definitions, windows, primary samples, DIVA-oriented questions (if any).
3. Extract sample and clinical fields; apply P03 review requirements for phenotype labels.
4. Harmonise `result_category` and link repeats.
5. Compute descriptive concordance and phenotype tables with uncertainty intervals (P06).
6. Apply P01 release tiering; prefer aggregates for Tier A.
7. Archive freeze artefacts; route corrections through P01.

## 11. Required field references

Diagnostic sample table (all core fields listed in Section 5); clinical event fields for phenotype, certainty, severity, outcome, veterinary review; bird registry species and release class; provenance fields.

## 12. Quality checks

- No public document in this workstream contains culture, propagation, genetic modification, or gain-of-function content.
- Every positive/negative claim carries QC and method context.
- Phenotype labels used in confirmatory tables are veterinary-reviewed.
- Repeat groups have consistent bird IDs and ordered timestamps.
- Species are not pooled without justification.

## 13. Responsible roles

| Role | Responsibilities |
|---|---|
| Avian veterinarian | Phenotype classification; clinical sampling indication; interpretation oversight |
| Data steward / surveillance steward | Metadata completeness; repeat linkage; P01 tiering |
| Collaborating diagnostic laboratory (authorised) | Assay performance under its quality system (external to this repo’s methods detail) |
| Analyst | Concordance, selection-bias diagnostics, uncertainty reporting |
| Project leads | Ensure public outputs remain within the biosafety boundary; approve institutional surveillance releases |

## 14. Limitations

- Managed-population surveillance is not a random community sample.
- Assay platforms differ; unvalidated cut-points travel poorly across methods.
- Marker presence is not synonymous with clinical PDD.
- Observational associations between markers and phenotype are hypothesis-generating unless designed for stronger inference.
- This protocol deliberately under-specifies laboratory methods to respect open-science risk boundaries.

## 15. Change control

| Version | Date | Summary |
|---|---|---|
| v0.1.0 | 2026-07-30 | Initial high-level ABV surveillance governance protocol with explicit biosafety boundary |

Any proposal to add laboratory manipulation content is a **protocol rejection criterion** for public files. Definitional changes to case grades or result harmonisation require version bumps and migration notes. Silently changing definitions is not permitted.
