# P01 — Data Governance and De-identification

> ## Experimental Demonstration Repository
>
> This is an early stage, nonproduction demonstration of proposed research methods, schemas, synthetic data and analysis workflows. It does not contain validated Sunshine BirdWorld research findings unless expressly stated. Sunshine BirdWorld’s substantive scientific work is ordinarily communicated through peer reviewed journals, veterinary and avicultural publications, books, conferences and established scientific forums. The material must not be used for veterinary, clinical, husbandry, conservation, legal or regulatory decisions without independent expert review. Sensitive operational information is intentionally excluded.

| Metadata | Value |
|---|---|
| **Protocol ID** | P01 |
| **Title** | Data Governance and De-identification |
| **Version** | v0.1.0 |
| **Effective date** | 2026-07-30 |
| **Status** | Active |
| **Parent documents** | [`RESEARCH_SCOPE.md`](../RESEARCH_SCOPE.md), [`DATA_DICTIONARY.md`](../DATA_DICTIONARY.md) |
| **Licence** | Documentation: CC BY 4.0; code: Apache-2.0 |

## 1. Purpose

This protocol defines operational rules for classifying, de-identifying, reviewing, releasing, correcting, and withdrawing Sunshine BirdWorld avian research records. No public dataset is released merely because it exists. Every release must satisfy scientific validity, animal-welfare integrity, privacy protection, facility-security protection, regulatory compliance, minimum necessary disclosure, provenance traceability, and correction readiness.

## 2. Scope

### In scope

- Assignment of release tiers A, B, and C consistent with the data dictionary.
- De-identification and generalisation steps before public or controlled scientific release.
- Fields and record classes that must never enter the public repository.
- Pre-release review checklist.
- Provenance and verification requirements.
- Post-release correction and withdrawal process.
- Minimum necessary disclosure for each scientific question.

### Out of scope

- Clinical treatment decisions.
- Laboratory biosafety authorisations.
- Legal advice on CITES, wildlife, or employment law (legal counsel is consulted when those obligations are material).
- Unrestricted publication of synthetic demonstration outputs as if they were institutional results.

> **Synthetic data notice.** Synthetic demonstration datasets and notebook outputs are teaching and reproducibility artefacts. They are not Sunshine BirdWorld results and must carry an explicit synthetic label in filenames, README text, table captions, and manuscript methods.

## 3. Release tiers (A / B / C)

Release class is assigned at the record or field level using `data_release_class` and `release_status` from the data dictionary. Tier assignment is conservative: if a record could reasonably fall into two tiers, assign the more restricted tier.

### Tier A — Fully public

Eligible content includes:

- synthetic examples and clearly labelled demonstration datasets;
- analysis code, schemas, validation rules, and notebooks;
- aggregate counts and proportions with denominators large enough that individuals are not re-identifiable;
- high-level protocols and reporting templates;
- de-identified analysis tables with negligible re-identification and security risk after the checklist in Section 6.

Tier A releases may be committed to the public GitHub repository and cited freely under the dual licence (Apache-2.0 for code; CC BY 4.0 for documentation and original synthetic data).

### Tier B — Controlled scientific access

Eligible content includes:

- granular dates that enable longitudinal reconstruction;
- rare-species individual histories;
- linked clinical–diagnostic–treatment trajectories;
- detailed assay results beyond aggregate positivity rates;
- combinations of fields that become identifying when joined.

Tier B material is shared only under a written data-use understanding that states purpose, retention, no-redistribution, no-reidentification, and destruction or return at project end. Tier B files are not placed in the public repository root without a further, documented de-identification reduction to Tier A.

### Tier C — Internal only

Never published or shared outside authorised institutional roles:

- human names, phone numbers, emails (other than the published institutional contact), addresses, and staff schedules;
- access credentials, badge IDs, and alarm or camera details;
- exact enclosure maps, GPS points, and anti-poaching system descriptions;
- source register numbers and unsalted internal identifiers;
- legal correspondence and commercial transaction details;
- unrestricted free-text clinical or treatment notes;
- raw surveillance video;
- animal-transfer details that create security or trafficking risk.

## 4. Fields never to publish

The following must be stripped, hashed with a private salt retained only internally, generalised, or withheld before any Tier A release:

| Category | Examples (dictionary-aligned) | Action |
|---|---|---|
| Direct human identifiers | staff names, visitor names, client contacts | Remove |
| Internal animal keys | raw register numbers; unsalted `restricted_source_id_hash` inputs | Hash internally; never publish salt |
| Exact location | precise GPS, building maps, camera positions | Replace with generalised `zone_id` |
| Security operations | access routes, response protocols, anti-poaching measures | Exclude |
| Sensitive free text | `clutch_notes_restricted`, `signs_free_text_restricted`, unrestricted treatment narratives | Keep Tier C |
| Dose detail without justification | `dose_value` / `dose_unit` combinations | Restrict unless scientifically necessary and reviewed |
| Transfer logistics | destination identity, transport routes, commercial terms | Generalise to `origin_category` / high-level movement flags only |
| Credentials and infrastructure | passwords, API keys, sensor network topology | Exclude |

Public `bird_id`, `pair_id`, `clutch_id`, `egg_id`, and `zone_id` values must be pseudonymous and stable within a release version, but must not encode register numbers, owner names, or map coordinates.

## 5. De-identification procedure

Perform steps in order. Document each step in the release package’s provenance statement.

1. **Define the scientific question and unit of analysis.** Record which fields are necessary (Section 8).
2. **Inventory source tables.** List entity types (bird, pair, clutch, egg, clinical event, sample, treatment, environmental interval, biosecurity event).
3. **Assign release class.** Set `data_release_class` and provisional `release_status = review_pending`.
4. **Remove Tier C fields.** Drop columns listed in Section 4; retain only hashed source links where scientific audit requires them.
5. **Pseudonymise identifiers.** Replace internal keys with public IDs. Preserve join integrity across tables within the freeze. Store the mapping table as Tier C.
6. **Generalise geography and zones.** Map enclosures to project-approved generalised `zone_id` codes (for example nursery, incubation, quarantine, outdoor_flight_group) without publishing a reverse map.
7. **Reduce date precision where needed.** For rare species or small strata, coarsen to month or season if exact dates enable re-identification or security inference; record precision in `hatch_date_precision` or an analogous field.
8. **Suppress small cells.** Do not publish cross-tabulations where a cell count is so small that an individual bird or pair is identifiable in context (default threshold: review any cell with count &lt; 5, and any rare-species row regardless of count).
9. **Scrub free text.** Remove names, places, phone numbers, and operational secrets from any residual notes intended for Tier A; prefer controlled vocabularies over free text.
10. **Validate joins and logic.** Run dictionary validation rules; resolve duplicates; confirm missingness codes are distinct from zeros.
11. **Label data origin.** Mark synthetic versus real institutional data explicitly.
12. **Complete the Section 6 checklist** and obtain required role sign-offs before changing `release_status` to `public` or `aggregate_only`.

## 6. Pre-release review checklist

A Tier A or aggregate public release may proceed only when every item is checked and dated:

- [ ] Scientific question, unit of analysis, numerator, and denominator are stated.
- [ ] Inclusion and exclusion counts are reported; exclusions are not used to favour a preferred conclusion.
- [ ] Critical fields meet the ≥95% completeness target unless the study is explicitly about missingness.
- [ ] No Tier C fields remain in the release package.
- [ ] Pseudonym map and salt are absent from the public artefact.
- [ ] Zone and location fields are generalised.
- [ ] Small-cell and rare-species disclosure risk has been reviewed.
- [ ] Animal-welfare context does not incentivise harmful replication.
- [ ] Regulatory obligations (wildlife, CITES, veterinary, laboratory, institutional) have been considered.
- [ ] Minimum necessary disclosure is documented (Section 8).
- [ ] Provenance fields are populated (Section 7).
- [ ] Verification status is at least `single_checked` for critical outcome fields; `double_checked` preferred for manuscript tables.
- [ ] Synthetic versus real labelling is unambiguous.
- [ ] Limitations section is drafted.
- [ ] Correction contact (`info@sunshinebirdworld.org`) is present in the release notes.
- [ ] Data steward and project lead (or delegated reviewer) have recorded approval.

## 7. Provenance requirements

Every research table, or a linked audit table, must carry the provenance fields defined in the data dictionary:

- `record_created_at`, `record_updated_at`
- `entered_by_role`
- `source_record_type`, `source_record_id_hash`
- `verification_status`, `verified_by_role`, `verification_date`
- `missingness_reason` where applicable
- `data_version`
- `release_status`
- `correction_note` after any post-freeze change

A public release package must also include:

- data cutoff date;
- protocol and dictionary versions used;
- count of source records reviewed, included, excluded, and duplicated;
- software environment reference (see P06);
- statement that synthetic demonstration data, if present, are not institutional results.

Source authenticity is never assumed. `verification_status = unverified` records may be used in exploratory work but must not anchor confirmatory claims without disclosure.

## 8. Minimum necessary disclosure

For each release, the data steward lists:

1. the scientific question;
2. the candidate field list;
3. fields removed as unnecessary;
4. fields retained and why each is required for the estimate, figure, or validation check.

Examples of minimum necessary practice:

- A fertility and hatchability table needs egg-level outcome fields and strata (`species_scientific`, `season`, `incubation_method`), not treatment doses or staff identities.
- A syndrome surveillance aggregate needs counts by `signs_controlled` and time window, not free-text notes or exact enclosure maps.
- An environmental association study needs generalised `zone_id`, interval summaries, and excursion flags, not sensor network topology or power-room locations.

If a field is interesting but not required, it stays internal or Tier B.

## 9. Correction and withdrawal process

1. **Report.** Errors may be reported to `info@sunshinebirdworld.org` or via a GitHub issue in [avian-research](https://github.com/sunshinebirdworld/avian-research).
2. **Triage.** Data steward classifies severity: cosmetic, analytic-impacting, privacy/security, or welfare-related.
3. **Contain.** If privacy or security is implicated, remove or replace the public artefact immediately and set `release_status = withdrawn` for affected records.
4. **Correct.** Edit the authoritative internal dataset; set `record_updated_at`; write `correction_note`; bump `data_version`.
5. **Propagate.** Re-run affected notebooks under P06; archive prior outputs; publish a short correction notice stating what changed and whether conclusions move.
6. **Do not silent-edit.** Historical DOI-like release tags, if used, remain immutable; issue a new version instead of rewriting history.

Records must not be deleted solely because they weaken a preferred conclusion. Analytic exclusions are coded with `exclusion_reason` and counted.

## 10. Required field references

Primary dictionary sections: Core bird registry (`data_release_class`, `zone_id`, `restricted_source_id_hash`); Provenance and release fields; Recommended public-release tiers A/B/C; entity-specific restricted free-text fields.

## 11. Quality checks

- Automated scan for forbidden patterns (emails, phone-like strings, GPS-like coordinates) in candidate Tier A files.
- Join integrity check across pseudonymous IDs after mapping.
- Verification that synthetic files contain an explicit synthetic marker in metadata or README.
- Manual rare-species disclosure review by data steward and project lead.
- Confirmation that `release_status` transitions are auditable.

## 12. Responsible roles

| Role | Responsibilities |
|---|---|
| Data steward | Tier assignment, de-identification execution, checklist completion, correction triage |
| Avian veterinarian | Welfare and clinical-sensitivity review for clinical/diagnostic releases |
| Analyst / statistician | Confirms denominators, small-cell risk in tables, analytic necessity of fields |
| Project leads (Dr. Debashis Banerjee; Dr. Anindita Banerjee) | Final public-release approval for institutional datasets; contact escalation |
| External collaborator (Tier B) | Bound by data-use terms; no redistribution |

## 13. Limitations

- De-identification reduces but does not eliminate re-identification risk, especially for rare species and linked longitudinal data.
- Aggregate tables can still disclose sensitive operations if strata are too fine.
- Regulatory landscapes change; a prior Tier A decision does not permanently authorise identical future releases.
- This protocol does not replace formal ethics, veterinary, or legal review when those are required.

## 14. Change control

| Version | Date | Summary |
|---|---|---|
| v0.1.0 | 2026-07-30 | Initial public protocol aligned with Research Scope and Data Dictionary |

Changes to tier definitions, forbidden-field lists, or checklist requirements require a version bump, migration note for in-flight releases, and update to this change-control table. Silently changing definitions is not permitted.
