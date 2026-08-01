# Data Dictionary

## 1. Purpose and conventions

This dictionary defines a harmonised structure for avian breeding, clinical, diagnostic, and environmental research records.

### General rules

- Column names use `snake_case`.
- Dates use ISO 8601: `YYYY-MM-DD`.
- Date-times use ISO 8601 with time zone: `YYYY-MM-DDThh:mm:ss+05:30`.
- Unknown values are blank/`NA`; do not use zero as a missing value.
- `not_applicable`, `not_recorded`, `not_performed`, and `unknown` are distinct states.
- Public identifiers are pseudonymous and must not expose register numbers, owner names, or security-sensitive locations.
- Every derived variable must be reproducible from documented source variables.
- Free text should be minimised in analysis tables and retained in a restricted source layer when necessary.

## 2. Entity relationships

```text
individual_bird
  ├── clinical_event
  │     ├── diagnostic_sample
  │     └── treatment_course
  ├── movement_event
  └── breeding_pair_member

breeding_pair
  └── clutch
        └── egg
              └── chick / individual_bird

environmental_interval
  └── enclosure_or_zone

equipment_event
  └── enclosure_or_zone
```

## 3. Core bird registry

| Field | Type | Required | Allowed values / format | Definition |
|---|---|---:|---|---|
| `bird_id` | string | yes | pseudonymous unique ID | Stable public or analysis identifier for one bird. |
| `restricted_source_id_hash` | string | restricted | salted hash | Link to internal source identifier; never publish the salt. |
| `species_scientific` | string | yes | accepted binomial | Scientific name used for the analysis version. |
| `species_common` | string | recommended | controlled text | Common name used in project documentation. |
| `taxonomy_source` | string | recommended | source and version | Taxonomic authority used. |
| `sex` | category | yes | `male`, `female`, `undetermined`, `unknown` | Sex at the time of the relevant record. |
| `sex_method` | category | no | `molecular`, `anatomical`, `clinical`, `recorded_history`, `unknown` | Basis of sex classification. |
| `hatch_date` | date | no | ISO date | Confirmed date of hatch. |
| `hatch_date_precision` | category | yes if date used | `exact`, `month`, `year`, `estimated` | Precision of the date. |
| `origin_category` | category | yes | `hatched_on_site`, `lawful_transfer`, `imported_lawfully`, `historical_unknown`, `other` | High-level origin without publishing sensitive transaction details. |
| `sire_id` | string | no | bird ID | Pseudonymous sire identifier. |
| `dam_id` | string | no | bird ID | Pseudonymous dam identifier. |
| `current_status` | category | yes | `alive_on_site`, `transferred`, `deceased`, `unknown` | Status at the dataset cutoff. |
| `status_date` | date | yes | ISO date | Date on which current status was established. |
| `zone_id` | string | restricted/public-generalised | controlled code | Generalised housing or research zone. |
| `data_release_class` | category | yes | `public`, `aggregate_only`, `restricted`, `excluded` | Maximum permitted release level. |

## 4. Breeding pair table

| Field | Type | Required | Allowed values / format | Definition |
|---|---|---:|---|---|
| `pair_id` | string | yes | unique pseudonymous ID | One defined breeding pair or breeding group. |
| `species_scientific` | string | yes | binomial | Species assigned to the pair. |
| `male_bird_id` | string | conditional | bird ID | Male member where applicable. |
| `female_bird_id` | string | conditional | bird ID | Female member where applicable. |
| `pair_start_date` | date | no | ISO date | First date pair was established. |
| `pair_end_date` | date | no | ISO date | Date pair ended. |
| `pairing_status` | category | yes | `active`, `inactive`, `historical`, `unknown` | Pair state at cutoff. |
| `pair_structure` | category | yes | `one_to_one`, `group`, `unknown` | Structure relevant to parentage certainty. |
| `parentage_confidence` | category | yes | `confirmed_genetic`, `confirmed_observational`, `probable`, `unknown` | Confidence in assigned parentage. |

## 5. Clutch table

| Field | Type | Required | Allowed values / format | Definition |
|---|---|---:|---|---|
| `clutch_id` | string | yes | unique ID | Eggs treated as belonging to one laying sequence. |
| `pair_id` | string | yes | pair ID | Parent pair or group. |
| `clutch_start_date` | date | yes | ISO date | Date first egg was laid or first observed. |
| `clutch_size_total` | integer | yes | ≥1 | Total eggs documented in the clutch. |
| `season_label` | string | no | prespecified code | Project-defined season or breeding period. |
| `incubation_strategy` | category | yes | `parental`, `artificial`, `mixed`, `unknown` | Overall incubation strategy. |
| `clutch_notes_restricted` | string | no | restricted free text | Operational context not intended for public release. |

## 6. Egg and hatch table

This is the main table used by the demonstration notebook.

| Field | Type | Required | Allowed values / format | Definition |
|---|---|---:|---|---|
| `egg_id` | string | yes | unique ID | One egg. |
| `clutch_id` | string | yes | clutch ID | Parent clutch. |
| `pair_id` | string | yes | pair ID | Parent pair or breeding group. |
| `species_scientific` | string | yes | binomial | Species. |
| `species_common` | string | recommended | controlled text | Common name. |
| `lay_date` | date | yes | ISO date | Date laid; estimated dates must be flagged. |
| `season` | category | yes | project-defined | Analysis stratum fixed before analysis. |
| `incubation_method` | category | yes | `parental`, `artificial`, `mixed`, `unknown` | Method used for most of incubation. |
| `initial_weight_g` | decimal | no | >0 | First standardised egg weight in grams. |
| `fertility_status` | category | yes | `fertile`, `infertile`, `unknown`, `not_assessed` | Fertility classification under project rules. |
| `fertility_basis` | category | recommended | `candling`, `breakout_exam`, `imaging`, `hatch`, `combined`, `unknown` | Basis of classification. |
| `embryo_loss_stage` | category | yes | `none`, `early`, `middle`, `late`, `unknown`, `not_applicable` | Stage of embryo death where a fertile egg did not hatch. |
| `hatch_status` | category | yes | `hatched`, `not_hatched`, `unknown` | Whether a live hatch occurred under the protocol definition. |
| `hatch_date` | date | conditional | ISO date | Required when hatched. |
| `hatch_assistance` | category | yes | `none`, `partial`, `full`, `unknown`, `not_applicable` | Degree of documented assistance. |
| `chick_id` | string | conditional | bird ID | Required where a stable chick identity exists. |
| `chick_status_day7` | category | yes | `alive`, `died`, `lost_to_followup`, `unknown`, `not_applicable` | Status seven completed days after hatch. |
| `exclusion_reason` | category | no | controlled code | Reason excluded from a specific analysis. |
| `data_quality_flag` | category | yes | `ok`, `review`, `exclude` | Data-review status. |
| `source_record_type` | category | yes | `register`, `spreadsheet`, `incubator_log`, `clinical_note`, `combined` | Primary provenance. |
| `verified_status` | category | yes | `unverified`, `single_checked`, `double_checked` | Verification level. |

### Logical validation rules for egg records

1. `egg_id` must be unique.
2. `hatch_status = hatched` requires `fertility_status = fertile`.
3. `hatch_status = hatched` requires a `hatch_date`.
4. `hatch_date` cannot precede `lay_date`.
5. `chick_status_day7` is applicable only to hatched eggs.
6. `embryo_loss_stage` is `not_applicable` for infertile eggs.
7. A fertile, non-hatched egg should have a loss stage or `unknown`.
8. `initial_weight_g` must be positive and biologically plausible for that species; species-specific limits belong in a validation table, not hard-coded globally.
9. `exclusion_reason` must be present when `data_quality_flag = exclude`.

## 7. Clinical event table

| Field | Type | Required | Allowed values / format | Definition |
|---|---|---:|---|---|
| `clinical_event_id` | string | yes | unique ID | One clinically coherent episode. |
| `bird_id` | string | yes | bird ID | Affected individual. |
| `event_start_datetime` | datetime | yes | ISO with time zone | First recognised onset or presentation. |
| `event_end_datetime` | datetime | no | ISO with time zone | Resolution, death, transfer, or cutoff. |
| `presentation_context` | category | yes | `routine`, `acute`, `surveillance`, `post_hatch`, `quarantine`, `other` | Context of evaluation. |
| `body_weight_g` | decimal | recommended | >0 | Standardised measured body weight. |
| `body_condition_score` | string | no | protocol-specific | Scale and version must be stated. |
| `signs_controlled` | array/string | yes | controlled vocabulary | Standardised observed clinical signs. |
| `signs_free_text_restricted` | string | no | restricted | Original detail for internal review. |
| `provisional_diagnosis` | string | no | controlled text | Working diagnosis. |
| `final_diagnosis` | string | no | controlled text | Best supported diagnosis at closure. |
| `diagnostic_certainty` | category | yes | `confirmed`, `probable`, `possible`, `unresolved` | Strength of evidence. |
| `severity` | category | yes | `mild`, `moderate`, `severe`, `critical`, `unknown` | Prespecified clinical severity. |
| `outcome` | category | yes | `resolved`, `improved`, `unchanged`, `worsened`, `recurred`, `died`, `euthanised`, `ongoing`, `lost_to_followup` | Episode outcome. |
| `outcome_date` | date | no | ISO date | Date outcome established. |
| `veterinary_review_status` | category | yes | `reviewed`, `pending`, `not_available` | Human professional review. |
| `adverse_event_flag` | boolean | yes | true/false | Whether a treatment-associated adverse event was recorded. |

## 8. Diagnostic sample table

| Field | Type | Required | Allowed values / format | Definition |
|---|---|---:|---|---|
| `sample_id` | string | yes | unique ID | One collected specimen. |
| `bird_id` | string | conditional | bird ID | Source individual where applicable. |
| `clinical_event_id` | string | no | event ID | Linked episode. |
| `collection_datetime` | datetime | yes | ISO with time zone | Collection time. |
| `sample_type` | category | yes | e.g. `whole_blood`, `plasma`, `serum`, `cloacal_swab`, `choanal_swab`, `faeces`, `tissue`, `other` | Specimen type. |
| `collection_context` | category | yes | `clinical`, `routine_surveillance`, `contact_investigation`, `research`, `post_mortem` | Why collected. |
| `target_name` | string | yes | assay target | Organism, antigen, antibody, gene target, chemistry, or pathology endpoint. |
| `assay_method` | string | yes | method and version | Diagnostic platform. |
| `laboratory_id` | string | yes | pseudonymous lab code | Testing laboratory. |
| `result_category` | category | yes | `positive`, `negative`, `inconclusive`, `invalid`, `not_tested` | Harmonised result. |
| `result_value` | decimal/string | no | assay-specific | Numeric or coded raw result. |
| `result_unit` | string | no | UCUM where possible | Unit. |
| `ct_value` | decimal | no | assay-specific | Cycle threshold where applicable. |
| `reference_interval` | string | no | assay-specific | Laboratory reference interval. |
| `qc_status` | category | yes | `passed`, `failed`, `not_reported` | Quality-control interpretation. |
| `report_date` | date | yes | ISO date | Date final report issued. |
| `repeat_sample_group_id` | string | no | group ID | Links serial samples for one question. |
| `interpretation_status` | category | yes | `raw_only`, `laboratory_interpreted`, `veterinary_interpreted` | Review level. |

## 9. Treatment course table

| Field | Type | Required | Allowed values / format | Definition |
|---|---|---:|---|---|
| `treatment_course_id` | string | yes | unique ID | One defined treatment course. |
| `clinical_event_id` | string | yes | event ID | Linked episode. |
| `agent_generic_name` | string | yes | generic name | Medication, fluid, nutritional, procedural, or supportive intervention. |
| `indication` | string | yes | controlled text | Reason used. |
| `route` | category | no | controlled | Route where relevant. |
| `dose_value` | decimal | restricted/conditional | >0 | Recorded dose; public release requires scientific justification. |
| `dose_unit` | string | conditional | explicit unit | Never release a dose without its unit and context. |
| `frequency` | string | no | explicit schedule | As recorded. |
| `start_datetime` | datetime | yes | ISO | Start. |
| `end_datetime` | datetime | no | ISO | End. |
| `prescriber_role` | category | yes | `avian_veterinarian`, `veterinarian`, `other_authorised_role`, `unknown` | Role, not identity. |
| `response_category` | category | yes | `improved`, `no_change`, `worsened`, `uncertain`, `not_assessed` | Recorded response. |
| `adverse_event` | boolean | yes | true/false | Suspected adverse event. |
| `causality_assessment` | category | no | `unlikely`, `possible`, `probable`, `unassessed` | Causality strength. |

## 10. Environmental interval table

| Field | Type | Required | Allowed values / format | Definition |
|---|---|---:|---|---|
| `environment_record_id` | string | yes | unique ID | One time-bounded measurement record. |
| `zone_id` | string | yes | generalised code | Nursery, incubation, quarantine, or enclosure zone. |
| `timestamp_start` | datetime | yes | ISO | Interval start. |
| `timestamp_end` | datetime | yes | ISO | Interval end. |
| `temperature_c_mean` | decimal | no | plausible range | Mean temperature. |
| `temperature_c_min` | decimal | no | plausible range | Minimum. |
| `temperature_c_max` | decimal | no | plausible range | Maximum. |
| `relative_humidity_pct_mean` | decimal | no | 0–100 | Mean relative humidity. |
| `co2_ppm_mean` | decimal | no | ≥0 | Mean carbon dioxide where measured. |
| `power_state` | category | yes | `grid`, `ups`, `generator`, `interrupted`, `unknown` | Dominant power state. |
| `sensor_id` | string | yes | pseudonymous code | Device identifier. |
| `sensor_calibration_status` | category | yes | `in_date`, `expired`, `unknown`, `not_applicable` | Calibration status. |
| `data_completeness_pct` | decimal | yes | 0–100 | Expected samples received. |
| `excursion_flag` | boolean | yes | true/false | Prespecified environmental deviation. |

## 11. Biosecurity event table

| Field | Type | Required | Allowed values / format | Definition |
|---|---|---:|---|---|
| `biosecurity_event_id` | string | yes | unique ID | One cleaning, disinfection, quarantine, or breach event. |
| `zone_id` | string | yes | generalised zone | Affected area. |
| `event_datetime` | datetime | yes | ISO | Event time. |
| `event_type` | category | yes | `routine_cleaning`, `terminal_disinfection`, `quarantine_entry`, `quarantine_exit`, `movement`, `breach`, `corrective_action`, `other` | Event class. |
| `agent_or_method` | string | no | controlled/generalised | Disinfectant or process where scientifically necessary. |
| `contact_time_minutes` | decimal | no | ≥0 | Recorded contact time. |
| `completed_as_planned` | boolean | yes | true/false | Protocol adherence. |
| `deviation_category` | string | no | controlled | Type of deviation. |
| `corrective_action` | string | no | restricted/generalised | Action taken. |
| `verified_by_role` | category | yes | staff role | Verification role, not identity. |

## 12. Provenance and release fields

These fields should appear in every research table or in a linked audit table.

| Field | Type | Required | Definition |
|---|---|---:|---|
| `record_created_at` | datetime | yes | When the electronic record was created. |
| `record_updated_at` | datetime | yes | Most recent change. |
| `entered_by_role` | category | yes | Role of original data entry. |
| `source_record_type` | category | yes | Register, clinical note, laboratory report, sensor, etc. |
| `source_record_id_hash` | string | yes | Pseudonymous source link. |
| `verification_status` | category | yes | Unverified, single-checked, or double-checked. |
| `verified_by_role` | category | no | Reviewer role. |
| `verification_date` | date | no | Review date. |
| `missingness_reason` | category | no | `not_recorded`, `not_applicable`, `not_performed`, `lost`, `unknown`. |
| `data_version` | string | yes | Dataset version. |
| `release_status` | category | yes | `internal`, `review_pending`, `aggregate_only`, `public`, `withdrawn`. |
| `correction_note` | string | no | Reason for a post-freeze correction. |

## 13. Core derived metrics

Let:

- \(N\) = all eligible eggs;
- \(N_A\) = eggs with assessable fertility;
- \(F\) = fertile eggs;
- \(H\) = live hatches;
- \(S_7\) = chicks alive at day 7 among those with known status.

Then:

- **Fertility rate** = \(F / N_A\)
- **Overall hatch rate** = \(H / N\)
- **Hatchability of fertile eggs** = \(H / F\)
- **Seven-day survival among known outcomes** = \(S_7 / (S_7 + D_7)\)

Every table must print both numerator and denominator. A percentage without its denominator is incomplete.

## 14. Recommended public-release tiers

### Tier A — Fully public

- synthetic examples;
- code;
- schemas;
- aggregate counts;
- high-level protocols;
- de-identified data with negligible re-identification and security risk.

### Tier B — Controlled scientific access

- granular dates;
- rare-species individual histories;
- linked longitudinal records;
- detailed diagnostics;
- potentially identifiable combinations.

### Tier C — Internal only

- names and contact details;
- exact locations;
- security systems;
- source register numbers;
- legal or private correspondence;
- unrestricted treatment notes;
- access credentials;
- raw video surveillance.

## 15. Change control

Any change to a field definition must include:

- date;
- previous definition;
- new definition;
- reason;
- expected effect on historical analyses;
- migration rule;
- reviewer.

Silently changing a definition is not permitted.
