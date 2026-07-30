# Research Protocols Index

> ## Experimental Demonstration Repository
>
> This is an early stage, nonproduction demonstration of proposed research methods, schemas, synthetic data and analysis workflows. It does not contain validated Sunshine BirdWorld research findings unless expressly stated. Sunshine BirdWorld’s substantive scientific work is ordinarily communicated through peer reviewed journals, veterinary and avicultural publications, books, conferences and established scientific forums. The material must not be used for veterinary, clinical, husbandry, conservation, legal or regulatory decisions without independent expert review. Sensitive operational information is intentionally excluded.

**Programme:** Sunshine BirdWorld Avian Research Methods  
**Institution:** Sunshine BirdWorld, rural West Bengal, India  
**Version:** v0.1.0  
**Effective date:** 2026-07-30  
**Licence:** Documentation under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); accompanying code under [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0).  
**Repository:** [https://github.com/sunshinebirdworld/avian-research](https://github.com/sunshinebirdworld/avian-research)

These protocols convert the programme boundaries in [`RESEARCH_SCOPE.md`](../RESEARCH_SCOPE.md) and the field definitions in [`DATA_DICTIONARY.md`](../DATA_DICTIONARY.md) into operational procedures for data stewardship, breeding-outcome measurement, clinical documentation, disease-surveillance governance, environmental logging, and reproducible analysis.

They are methods documents for open scientific practice. They do not authorise clinical treatment, laboratory pathogen work, or any procedure that requires a veterinarian, ethics committee, statutory permission, or biosafety oversight without those controls being separately in place.

> **Synthetic data notice.** Demonstration tables and notebook outputs in this repository use labelled synthetic data. Synthetic results are not Sunshine BirdWorld breeding, clinical, or surveillance findings and must not be cited as institutional evidence.

## Contact

**Sunshine BirdWorld**  
Rural West Bengal, India  
Email: [info@sunshinebirdworld.org](mailto:info@sunshinebirdworld.org)  
Website: [https://www.sunshinebirdworld.org](https://www.sunshinebirdworld.org)  
Project leads: Dr. Debashis Banerjee and Dr. Anindita Banerjee

## Protocol inventory

| ID | File | Purpose |
|---|---|---|
| P01 | [`P01_DATA_GOVERNANCE_AND_DEIDENTIFICATION.md`](P01_DATA_GOVERNANCE_AND_DEIDENTIFICATION.md) | Release tiers A/B/C, de-identification, fields never published, pre-release checklist, provenance, corrections, minimum necessary disclosure |
| P02 | [`P02_BREEDING_AND_HATCHING_OUTCOMES.md`](P02_BREEDING_AND_HATCHING_OUTCOMES.md) | Fertility, embryo-loss stages, hatch, assistance, day-7 survival; denominators; inclusion/exclusion; stratification; egg-table linkage |
| P03 | [`P03_CLINICAL_EVENT_DOCUMENTATION.md`](P03_CLINICAL_EVENT_DOCUMENTATION.md) | Clinical episode structure, controlled vocabularies, diagnostic certainty, severity, outcomes, treatment linkage, veterinary review, public exclusions |
| P04 | [`P04_AVIAN_BORNAVIRUS_SURVEILLANCE.md`](P04_AVIAN_BORNAVIRUS_SURVEILLANCE.md) | High-level avian bornavirus research governance: case definitions, sampling metadata, result categories, repeat testing, DIVA-oriented evidence questions; explicit biosafety boundary |
| P05 | [`P05_ENVIRONMENTAL_AND_BIOSECURITY_LOGGING.md`](P05_ENVIRONMENTAL_AND_BIOSECURITY_LOGGING.md) | Environmental intervals, power/equipment events, cleaning/disinfection/quarantine/breach logging; zone generalisation; outcome linkage without facility-security disclosure |
| P06 | [`P06_REPRODUCIBLE_ANALYSIS.md`](P06_REPRODUCIBLE_ANALYSIS.md) | Analysis freeze, notebook execution, software versioning, Wilson CIs, clustering caveats, sensitivity analyses, output archiving, synthetic vs real labelling |

## Recommended reading order

1. Read [`RESEARCH_SCOPE.md`](../RESEARCH_SCOPE.md) for aims, inclusions, exclusions, and non-claims.
2. Read [`DATA_DICTIONARY.md`](../DATA_DICTIONARY.md) for entities, fields, validation rules, and release tiers.
3. Read **P01** before creating or releasing any public table.
4. Read **P02** and/or **P03** and/or **P05** according to the workstream.
5. Read **P04** only for surveillance-governance and evidence-analysis design; it intentionally omits laboratory manipulation methods.
6. Read **P06** before freezing an analysis dataset or publishing notebook outputs.
7. Run the demonstration notebook only after understanding that its data are synthetic.

For a first-time contributor focused on breeding metrics, the shortest path is: Research Scope → Data Dictionary → P01 → P02 → P06 → notebook.

## Cross-cutting conventions

- Protocol versioning uses semantic versioning (`MAJOR.MINOR.PATCH`).
- Dates use ISO 8601 (`YYYY-MM-DD`); date-times include Asia/Kolkata offset (`+05:30`) unless a sensor system stores UTC and documents the conversion.
- Roles are named by function (data steward, avian veterinarian, analyst, project lead), not by personal identity, except where contact attribution is required.
- Every public scientific claim must state unit of analysis, numerator, denominator, data cutoff, and limitations.
- Observational associations are not causal claims without an appropriate design.

## Change control for this index

Material changes to protocol inventory, reading order, or licensing statements require an update to this file, a corresponding protocol version bump where definitions change, and a dated entry in each affected protocol’s change-control section. Silently revising definitions is not permitted.
