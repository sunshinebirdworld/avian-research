# P03 — Clinical Event Documentation

| Metadata | Value |
|---|---|
| **Protocol ID** | P03 |
| **Title** | Clinical Event Documentation |
| **Version** | v0.1.0 |
| **Effective date** | 2026-07-30 |
| **Status** | Active |
| **Parent documents** | [`RESEARCH_SCOPE.md`](../RESEARCH_SCOPE.md) Aim 3; [`DATA_DICTIONARY.md`](../DATA_DICTIONARY.md) clinical event, diagnostic sample, treatment course tables |
| **Licence** | Documentation: CC BY 4.0; code: Apache-2.0 |

## 1. Purpose

This protocol defines how Sunshine BirdWorld converts clinical observations into structured episodes suitable for descriptive case series, syndrome surveillance, diagnostic-yield analysis, treatment-response documentation, adverse-event review, and hypothesis generation. Retrospective records are labelled as retrospective. The protocol does not replace prospective controlled trials when those are required, and it does not authorise treatment without veterinary oversight.

## 2. Scope

### In scope

- Clinical episode structure and timeline rules.
- Controlled-vocabulary guidance for signs and diagnoses.
- Diagnostic certainty and severity coding.
- Episode outcomes and follow-up.
- Linkage to diagnostic samples and treatment courses.
- Veterinary review requirements.
- Rules for what must not enter public releases.

### Out of scope

- Prescribing protocols or dose nomograms for unsupervised use.
- Claiming that a structured retrospective series equals a randomised trial.
- Publishing identifiable staff, client, or exact-location clinical detail.
- Representing synthetic vignettes as real Sunshine BirdWorld case outcomes.

> **Synthetic data notice.** Any synthetic clinical examples released for schema testing are labelled synthetic and are not institutional case series evidence.

## 3. Clinical episode structure

A **clinical event** is one clinically coherent episode for one bird (`clinical_event_id` + `bird_id`).

### Episode construction rules

1. **Onset:** `event_start_datetime` is the first recognised onset or presentation (ISO 8601 with `+05:30` when local civil time is used).
2. **Closure:** `event_end_datetime` is resolution, death, euthanasia, transfer out of observation, or analysis cutoff for ongoing cases.
3. **Coherence:** New signs that are clearly a continuation or expected evolution of the same process stay in the same episode; a distinct new disease process after recovery starts a new `clinical_event_id`.
4. **Context:** Code `presentation_context` as `routine`, `acute`, `surveillance`, `post_hatch`, `quarantine`, or `other`.
5. **Measurements:** Record `body_weight_g` when obtained; if body-condition scoring is used, state scale name and version in the analysis plan.
6. **Signs:** Prefer `signs_controlled` (controlled vocabulary). Keep narrative detail in `signs_free_text_restricted` (Tier C / internal).
7. **Diagnoses:** Maintain `provisional_diagnosis` during work-up and `final_diagnosis` at closure when supported.
8. **Certainty, severity, outcome:** Required at analysis freeze for closed episodes; ongoing episodes may carry `outcome = ongoing` with certainty still set to the best current level.
9. **Review:** Set `veterinary_review_status` and `adverse_event_flag`.

One bird may have many episodes. Episodes may link zero or more diagnostic samples and zero or more treatment courses.

## 4. Controlled vocabulary guidance

### Principles

- Prefer a finite, versioned sign list over open prose for analysis tables.
- Use species-neutral terms where possible; add species-specific qualifiers only when clinically necessary.
- Map legacy free text to controlled terms during retrospective harmonisation; retain original text internally.
- Version the vocabulary (`signs_vocab_version`) in the analysis plan or a linked reference file when the list changes.

### Minimum sign domains (illustrative controlled set)

Projects should adopt an explicit list before confirmatory analysis. Core domains include:

- general: lethargy, anorexia, weight_loss, weakness;
- gastrointestinal: regurgitation, diarrhoea, undigested_feces, crop_stasis;
- neurological: ataxia, tremors, seizures, proprioceptive_deficits, blindness_suspected;
- respiratory: dyspnoea, nasal_discharge, tail_bobbing;
- feather/skin: feather_damaging_behaviour, pruritus, lesions;
- other: polyuria_polydipsia, sudden_death, postoperative_status.

Multiple signs per episode are allowed (array or delimited controlled string per dictionary practice). Absence of a sign is not coded unless systematically examined and recorded as negative under a prospective checklist.

### Diagnosis vocabulary

- Use controlled diagnostic phrases for `provisional_diagnosis` and `final_diagnosis`.
- Prefer syndrome labels when etiology is unproven (for example “proventricular dilatation syndrome–compatible clinical picture”) rather than overstating pathogen confirmation.
- Separate pathogen detection (sample table) from clinical diagnosis (event table).

## 5. Diagnostic certainty

| Value | Meaning |
|---|---|
| `confirmed` | Diagnosis supported by definitive evidence appropriate to the condition (for example pathognomonic pathology, validated laboratory confirmation plus compatible clinical picture, or equivalent). |
| `probable` | Strongly supported clinically ± supportive tests; alternative explanations unlikely but not fully excluded. |
| `possible` | Compatible but competing explanations remain plausible. |
| `unresolved` | Episode closed or truncated without a working etiological diagnosis. |

Certainty refers to the clinical diagnosis, not merely to a single assay result. A positive laboratory marker without clinical correlation does not automatically yield `confirmed` clinical disease.

## 6. Severity

| Value | Operational guidance |
|---|---|
| `mild` | Minimal systemic compromise; ambulatory; feeding; outpatient-level monitoring under veterinary judgement. |
| `moderate` | Clear illness with functional impact; may require active treatment and closer monitoring. |
| `severe` | Marked systemic compromise; substantial risk without intensive management. |
| `critical` | Life-threatening presentation or immediate risk of death. |
| `unknown` | Severity not recoverable from source records. |

Severity is assigned at peak severity during the episode unless the analysis plan states otherwise (for example admission severity). Document the rule used.

## 7. Outcomes

| Value | Definition |
|---|---|
| `resolved` | Clinical signs of the episode abated to baseline or clinically negligible. |
| `improved` | Partial improvement without full resolution. |
| `unchanged` | No meaningful change. |
| `worsened` | Clinical deterioration relative to presentation. |
| `recurred` | Return of the same process after documented resolution (may close prior episode and open a new one per construction rules; code recurrence consistently in the analysis plan). |
| `died` | Death attributed temporally to the episode context (cause attribution may remain uncertain). |
| `euthanised` | Euthanasia performed under veterinary authority. |
| `ongoing` | Still under observation at cutoff. |
| `lost_to_followup` | Outcome unknown after transfer or lost observation. |

Record `outcome_date` when known. Time-to-event analyses must prespecify zero time (presentation versus onset).

## 8. Treatment linkage

Each treatment course (`treatment_course_id`) links to exactly one `clinical_event_id` and records:

- `agent_generic_name`, `indication`, `route` (when relevant);
- `start_datetime` / `end_datetime`;
- `prescriber_role` (`avian_veterinarian`, `veterinarian`, `other_authorised_role`, `unknown`) — role, not personal identity;
- `response_category` (`improved`, `no_change`, `worsened`, `uncertain`, `not_assessed`);
- `adverse_event` and optional `causality_assessment`.

### Public handling of doses

`dose_value` and `dose_unit` are restricted by default (P01). Public release requires scientific justification, veterinary review, and context sufficient to prevent unsafe unsupervised replication. Aggregate statements such as “systemic antimicrobial administered” may be preferable to exact milligram schedules in Tier A outputs.

Set `adverse_event_flag` on the clinical event when any linked course records a suspected adverse event.

## 9. Diagnostic sample linkage

Samples link via `clinical_event_id` when collected in episode context. Required interpretive discipline:

- `result_category`: `positive`, `negative`, `inconclusive`, `invalid`, `not_tested`;
- `qc_status` and `interpretation_status` must be populated;
- distinguish raw laboratory output from veterinary interpretation;
- do not equate assay positivity alone with clinical disease.

Surveillance-only samples may omit `clinical_event_id` but must retain `collection_context`.

## 10. Veterinary review requirements

| Analysis use | Minimum `veterinary_review_status` |
|---|---|
| Internal exploratory tallies | `pending` allowed with disclosure |
| Institutional case series draft | `reviewed` for included episodes |
| Public Tier A clinical aggregates | `reviewed` for contributing episodes, or explicit limitation if historical notes cannot be re-reviewed |
| Adverse-event summaries | `reviewed` by avian veterinarian or veterinarian |

AI systems may draft structured extracts from notes but must not certify diagnosis, disposition, or treatment (see programme AI boundary). Human veterinary verification is required for confirmatory clinical claims.

## 11. What not to publish publicly

In addition to P01 Tier C rules, clinical public releases must not include:

- staff or client names and contact details;
- unrestricted free-text examination notes;
- exact enclosure or hospital-cage locations;
- photographs that identify protected locations or people without separate ethical clearance;
- full medication regimens that could encourage unsafe replication without veterinary oversight, unless justified and reviewed;
- legal or complaint correspondence;
- transfer destinations that create security risk.

Prefer aggregate syndrome counts, de-identified episode tables with controlled signs, and high-level outcome distributions for Tier A.

## 12. Procedure — from note to structured episode

1. Identify whether the presentation continues an open episode or starts a new `clinical_event_id`.
2. Enter onset, context, weight, and controlled signs; park narrative in restricted text.
3. Order or attach diagnostics with full sample metadata when tests are performed.
4. Record treatments as separate courses linked to the episode.
5. Update provisional diagnosis and certainty as evidence accrues.
6. At closure, set final diagnosis (if any), peak severity rule, outcome, outcome date, adverse-event flag.
7. Complete veterinary review status.
8. Run validation: end ≥ start; hatched-chick post_hatch context consistent with registry; treatment courses reference valid events.
9. Assign `data_release_class` / `release_status` under P01 before any external share.

## 13. Required field references

Clinical event table: `clinical_event_id`, `bird_id`, `event_start_datetime`, `event_end_datetime`, `presentation_context`, `body_weight_g`, `body_condition_score`, `signs_controlled`, `signs_free_text_restricted`, `provisional_diagnosis`, `final_diagnosis`, `diagnostic_certainty`, `severity`, `outcome`, `outcome_date`, `veterinary_review_status`, `adverse_event_flag`.

Linked tables: diagnostic sample fields; treatment course fields; bird registry identifiers and `data_release_class`.

## 14. Quality checks

- No orphan treatment courses or samples pointing to missing events (unless surveillance samples intentionally unlinked).
- Controlled signs validate against the vocabulary list.
- `confirmed` certainty requires documented evidence type in internal notes or linked samples.
- Adverse-event flags reconcile with treatment-course adverse-event fields.
- Missingness distinguished among not recorded, not performed, not applicable, and unknown.
- Retrospective versus prospective collection labelled at dataset level.

## 15. Responsible roles

| Role | Responsibilities |
|---|---|
| Attending avian veterinarian / veterinarian | Clinical diagnosis, severity, treatment authorisation, review sign-off |
| Clinical records steward | Structured entry, vocabulary mapping, provenance |
| Analyst | Case-series denominators, diagnostic-yield definitions, time-to-event coding |
| Data steward | De-identification and public-exclusion enforcement |
| Project leads | Approval of institutional clinical public aggregates |

## 16. Limitations

- Historical notes may lack systematic negative findings, biasing syndrome frequencies.
- Controlled vocabularies compress nuance; restricted text remains essential for clinical care but is not public evidence.
- Treatment response in uncontrolled settings confounds disease natural history with intervention effect.
- Single-centre case mix does not generalise to all avicultural settings.
- This protocol is not a licence to practise veterinary medicine from the repository text.

## 17. Change control

| Version | Date | Summary |
|---|---|---|
| v0.1.0 | 2026-07-30 | Initial public clinical documentation protocol |

Changes to certainty, severity, outcome, or episode-construction rules require a version bump, effect note for historical series, and migration guidance. Silently changing definitions is not permitted.
