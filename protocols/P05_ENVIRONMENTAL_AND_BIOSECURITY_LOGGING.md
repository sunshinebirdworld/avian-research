# P05 — Environmental and Biosecurity Logging

> ## Experimental Demonstration Repository
>
> This is an early stage, nonproduction demonstration of proposed research methods, schemas, synthetic data and analysis workflows. It does not contain validated Sunshine BirdWorld research findings unless expressly stated. Sunshine BirdWorld’s substantive scientific work is ordinarily communicated through peer reviewed journals, veterinary and avicultural publications, books, conferences and established scientific forums. The material must not be used for veterinary, clinical, husbandry, conservation, legal or regulatory decisions without independent expert review. Sensitive operational information is intentionally excluded.

| Metadata | Value |
|---|---|
| **Protocol ID** | P05 |
| **Title** | Environmental and Biosecurity Logging |
| **Version** | v0.1.0 |
| **Effective date** | 2026-07-30 |
| **Status** | Active |
| **Parent documents** | [`RESEARCH_SCOPE.md`](../RESEARCH_SCOPE.md) Aim 6; [`DATA_DICTIONARY.md`](../DATA_DICTIONARY.md) environmental interval, biosecurity event, equipment/power fields |
| **Licence** | Documentation: CC BY 4.0; code: Apache-2.0 |

## 1. Purpose

This protocol standardises logging of environmental intervals, power and equipment events, and cleaning, disinfection, quarantine, movement, and breach-related biosecurity events so that husbandry conditions can be linked to breeding, clinical, and surveillance outcomes. It requires zone generalisation and forbids publication of exact facility-security details while still enabling scientifically useful operational evidence.

## 2. Scope

### In scope

- Time-bounded environmental interval records (temperature, humidity, optional CO₂, power state, sensor QC).
- Equipment and power interruption documentation relevant to incubation and nursery stability.
- Biosecurity event classes: routine cleaning, terminal disinfection, quarantine entry/exit, movement, breach, corrective action.
- Generalised `zone_id` coding for analysis and public release.
- Linkage rules to clutch, egg, chick, and clinical outcomes without disclosing maps or security systems.

### Out of scope

- Publishing enclosure blueprints, GPS coordinates, camera placements, access-control schematics, or anti-poaching measures.
- Claiming causal effect of a single cleaning product from uncontrolled observational data.
- Treating synthetic environmental demo series as real Sunshine BirdWorld operational telemetry.

> **Synthetic data notice.** Demonstration environmental rows, if present, are labelled synthetic and are not institutional climate or biosecurity performance results.

## 3. Zone generalisation

### Internal versus public zone identifiers

- **Internal layer (Tier C):** may use fine-grained location codes needed for husbandry.
- **Analysis / public layer:** map to generalised `zone_id` values that support scientific strata without revealing layout.

### Approved generalised zone families (project-controlled list)

Examples of public-safe families (exact list versioned internally):

- `incubation`
- `nursery`
- `quarantine`
- `hospital_isolation`
- `indoor_holding`
- `outdoor_flight_group`
- `food_prep`
- `other_generalised`

Rules:

1. Do not publish a reverse crosswalk from generalised zones to named buildings or GPS.
2. Merge zones when a stratum would identify a single sensitive area.
3. Season and species strata plus fine zone detail can become identifying; apply P01 small-cell review.
4. Sensor IDs in public data must be pseudonymous and must not encode room numbers.

## 4. Environmental interval logging

### Record unit

One `environment_record_id` covers `[timestamp_start, timestamp_end]` for one generalised `zone_id` and `sensor_id`.

### Required / core fields

- `zone_id`, `timestamp_start`, `timestamp_end`
- `temperature_c_mean` / `min` / `max` when temperature is in scope
- `relative_humidity_pct_mean` when humidity is in scope
- `co2_ppm_mean` when measured
- `power_state`: `grid`, `ups`, `generator`, `interrupted`, `unknown`
- `sensor_id`, `sensor_calibration_status` (`in_date`, `expired`, `unknown`, `not_applicable`)
- `data_completeness_pct`
- `excursion_flag` (true when values breach prespecified limits in the analysis plan or SOP)

### Procedure

1. Define sampling interval (for example 5–15 minutes raw; store analysis intervals as hourly or daily aggregates when releasing publicly).
2. Document sensor calibration status at interval creation or via linked device log.
3. Compute completeness as received samples / expected samples in the interval.
4. Flag excursions using written thresholds (species- and room-purpose-specific); do not improvise thresholds after seeing outcome associations in confirmatory work.
5. On power transition, update `power_state` and, if needed, open an equipment/power event record (Section 5).
6. Retain raw high-resolution feeds internally; release aggregated intervals under P01.

## 5. Power and equipment events

Document events that can plausibly affect incubation stability, chick comfort, or disinfection validity.

### Minimum event content (internal log → generalised analysis table)

- Event datetime (ISO with offset).
- Generalised zone(s) affected.
- Event class: power interruption, UPS engagement, generator start, incubator failure, HVAC failure, sensor outage, other.
- Duration if known.
- Corrective-action timestamp and whether conditions returned within target.
- Link to `excursion_flag` intervals where applicable.

Public summaries should prefer counts, durations, and outcome associations at generalised zone level—not panel schedules, contractor identities, or infrastructure schematics.

## 6. Biosecurity event logging

Use the biosecurity event table:

| Field | Role |
|---|---|
| `biosecurity_event_id` | Unique event |
| `zone_id` | Generalised zone |
| `event_datetime` | When the event occurred or was recognised |
| `event_type` | `routine_cleaning`, `terminal_disinfection`, `quarantine_entry`, `quarantine_exit`, `movement`, `breach`, `corrective_action`, `other` |
| `agent_or_method` | Controlled/generalised disinfectant or process name when scientifically necessary |
| `contact_time_minutes` | Recorded contact time |
| `completed_as_planned` | Protocol adherence |
| `deviation_category` | Controlled deviation code |
| `corrective_action` | Restricted/generalised description |
| `verified_by_role` | Role, not personal name |

### Breach events

A **breach** is a recorded failure of intended biosecurity control (for example unprotected movement between quarantine and nursery, incomplete disinfection contact time, or equipment reuse against SOP). Breaches require:

- factual description in the internal layer;
- corrective action;
- verification role;
- consideration of whether linked clinical or surveillance follow-up is needed (veterinary judgement).

Public Tier A outputs may report breach counts by generalised type and week/month; they must not describe exploitable security pathways.

### Quarantine and movement

Log quarantine entry/exit and movement events with generalised zones only in public extracts. Animal-transfer details that create trafficking or theft risk remain Tier C (P01).

## 7. Linkage to outcomes without security disclosure

### Permitted linkage keys

- Generalised `zone_id`
- Date or datetime windows
- Pseudonymous `clutch_id`, `egg_id`, `bird_id`, `clinical_event_id`

### Example analytic joins

- Egg incubation window ↔ incubation-zone temperature/humidity summaries ↔ hatchability.
- Nursery-zone excursion-hours in first 7 days ↔ `chick_status_day7`.
- Breach or quarantine-exit dates ↔ subsequent clinical-event incidence (descriptive).

### Forbidden in public linked tables

- Exact cage IDs that map to published photos or visitor paths.
- Staff rosters aligned to breach times.
- Camera or alarm metadata.
- Maps joining zone codes to coordinates.

Observational associations require non-causal language unless the design supports stronger inference (Research Scope statistical principles).

## 8. Procedure — daily to release

1. **Capture:** sensors write intervals; staff log cleaning/disinfection/quarantine/breach events the same operational day when feasible.
2. **Verify:** calibration status and `completed_as_planned` checks; escalate unresolved breaches.
3. **Curate:** map internal locations to generalised `zone_id`; set provenance fields.
4. **Link:** build analysis features (daily mean temperature, excursion-hours, days since terminal disinfection, power-interruption minutes) in a reproducible script (P06).
5. **Review:** data steward checks security leakage and small-cell risk (P01).
6. **Release:** aggregates and generalised interval summaries only when checklist-complete.

## 9. Required field references

Environmental interval table fields (dictionary Section 10); biosecurity event table fields (Section 11); provenance/release fields; egg/clinical identifiers used only as pseudonymous join keys; `power_state` and excursion flags as operational outcomes in Research Scope Section 6.

## 10. Quality checks

- `timestamp_end` ≥ `timestamp_start`.
- Humidity in 0–100; temperatures within plausible sensor ranges or flagged.
- `data_completeness_pct` documented; low-completeness intervals flagged before confirmatory use.
- Calibration expired ⇒ disclose or exclude from primary environmental exposure metrics.
- Biosecurity events have verification roles; breaches have corrective actions.
- Public files contain only generalised zones and pass automated scans for GPS-like strings (P01).

## 11. Responsible roles

| Role | Responsibilities |
|---|---|
| Facilities / husbandry operations role | Sensor upkeep, cleaning logs, immediate breach reporting |
| Nursery / incubation lead | Interpreting excursion impact on eggs and chicks |
| Avian veterinarian | Quarantine policy adherence; clinical follow-up after breaches |
| Data steward | Zone generalisation, linkage safety, release review |
| Analyst | Feature engineering, uncertainty, confounding discussion |
| Project leads | Approval of public operational aggregates |

## 12. Limitations

- Sensor failure and missing intervals can correlate with the very failures under study.
- Staff-reported cleaning logs may overstate adherence (`completed_as_planned`).
- Generalised zones reduce spatial resolution and can mix microclimates.
- Confounding by season, staffing, and species cohort is expected.
- Operational associations are not automatic proof of causation.

## 13. Change control

| Version | Date | Summary |
|---|---|---|
| v0.1.0 | 2026-07-30 | Initial environmental and biosecurity logging protocol with zone-generalisation rules |

Changes to event-type vocabularies, excursion definitions, or public zone families require a version bump, effect note, and migration rule. Silently changing definitions is not permitted.
