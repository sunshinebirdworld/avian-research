# Sunshine BirdWorld Avian Research Methods

**Open, reproducible methods for avian health, conservation breeding, disease surveillance, and evidence generation from managed avicultural populations.**

Sunshine BirdWorld is a long-running avicultural breeding and research centre in rural West Bengal, India. This repository is a public methods and reproducibility workspace for converting carefully documented field observations into transparent, reviewable, and reusable scientific outputs.

The repository is designed for veterinarians, avian researchers, conservation breeders, statisticians, data stewards, and responsible aviculturists. It is not a commercial product repository and does not contain trade secrets, customer data, live-animal sale information, precise facility-security details, or personally identifying information.

> **Repository status:** Early public release. The structure, schemas, and demonstration analysis are usable now, while project-specific datasets and manuscripts will be added only after scientific, welfare, privacy, and regulatory review.

## Why this repository exists

Avian medicine and conservation breeding often suffer from three related problems:

1. Rare species are represented by small and fragmented datasets.
2. Longitudinal observations remain in paper registers, spreadsheets, clinical notes, or institutional memory.
3. Published reports frequently omit the data definitions and analysis steps needed for independent review or reuse.

Sunshine BirdWorld maintains long-duration records across breeding, incubation, neonatal care, clinical events, disease surveillance, husbandry, and environmental operations. This repository creates a disciplined bridge between those records and publishable science.

The goal is not to present anecdote as proof. The goal is to make observational evidence:

- clearly defined;
- ethically governed;
- quality-checked;
- statistically honest;
- reproducible;
- open to correction;
- and useful beyond a single facility.

## Scientific mission

The programme focuses on non-commercial scientific work intended for peer discussion, peer review, reproducible analysis, and responsible public dissemination.

Current workstreams include:

- conservation-breeding and progeny outcome documentation;
- fertility, embryo-loss, hatchability, neonatal-survival, and growth analyses;
- retrospective avian clinical case series;
- disease surveillance in managed avian populations;
- high-level avian bornavirus research, including evaluation of DIVA-oriented research questions;
- biosecurity, environmental, and operational-risk documentation;
- species-specific husbandry evidence synthesis;
- research-data standards for aviculture in resource-constrained settings.

A detailed boundary of the programme is provided in [`RESEARCH_SCOPE.md`](RESEARCH_SCOPE.md).

## What is included

```text
.
├── README.md
├── RESEARCH_SCOPE.md
├── DATA_DICTIONARY.md
├── CONTRIBUTING.md
├── CITATION.cff
├── LICENSE.md
├── requirements.txt
├── data/
│   ├── README.md
│   └── example_breeding_events.csv
├── docs/
│   └── AI_USE_AND_VALIDATION.md
├── notebooks/
│   └── 01_breeding_outcomes_analysis.ipynb
├── outputs/
│   └── .gitkeep
├── protocols/
│   ├── README.md
│   ├── P01_DATA_GOVERNANCE_AND_DEIDENTIFICATION.md
│   ├── P02_BREEDING_AND_HATCHING_OUTCOMES.md
│   ├── P03_CLINICAL_EVENT_DOCUMENTATION.md
│   ├── P04_AVIAN_BORNAVIRUS_SURVEILLANCE.md
│   ├── P05_ENVIRONMENTAL_AND_BIOSECURITY_LOGGING.md
│   └── P06_REPRODUCIBLE_ANALYSIS.md
└── src/
    └── avian_metrics.py
```

## Demonstration analysis

The notebook [`notebooks/01_breeding_outcomes_analysis.ipynb`](notebooks/01_breeding_outcomes_analysis.ipynb) is an executable analysis of a clearly labelled **synthetic** dataset. It demonstrates the intended workflow without disclosing real institutional records.

It performs:

- schema and logical-consistency checks;
- duplicate and missingness review;
- calculation of fertility, overall hatch rate, hatchability of fertile eggs, and seven-day chick survival;
- Wilson 95% confidence intervals for proportions;
- stratified summaries by species and season;
- outcome visualisation;
- reproducible export of result tables and figures;
- a structured interpretation section that distinguishes observation from inference.

The notebook does **not** claim that the synthetic results describe Sunshine BirdWorld. Its purpose is to prove that the proposed data standard and analysis pipeline are real, executable, and reviewable.

## Quick start

Clone the repository and create a Python environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Open:

```text
notebooks/01_breeding_outcomes_analysis.ipynb
```

The notebook can be run from either the repository root or the `notebooks` directory. Outputs are written to `outputs/`.

## Data-governance principles

No public dataset will be released merely because it exists. Every release must pass the following checks:

1. **Scientific validity** — variables, denominators, exclusions, and limitations are documented.
2. **Animal welfare** — publication must not incentivise harmful replication or omit material welfare context.
3. **Privacy** — names, phone numbers, addresses, staff identifiers, client information, and private correspondence are excluded.
4. **Security** — enclosure locations, access systems, camera placement, critical infrastructure, and anti-poaching details are excluded or generalised.
5. **Regulatory compliance** — records are reviewed for applicable wildlife, CITES, veterinary, laboratory, and institutional obligations.
6. **Minimum necessary disclosure** — only fields required for the scientific question are released.
7. **Traceability** — released values retain a documented provenance and verification state.
8. **Correction readiness** — errors are corrected transparently, with version history preserved.

The operational rules are set out in [`protocols/P01_DATA_GOVERNANCE_AND_DEIDENTIFICATION.md`](protocols/P01_DATA_GOVERNANCE_AND_DEIDENTIFICATION.md).

## Responsible boundaries

This repository may contain surveillance designs, case definitions, metadata structures, and statistical methods. It does not publish:

- pathogen culture or propagation procedures;
- genetic modification or gain-of-function instructions;
- methods intended to increase pathogenicity, host range, immune evasion, or environmental persistence;
- unvalidated treatment directions for use without veterinary oversight;
- exact facility-security or animal-location information;
- identifiable staff, visitor, supplier, client, or complainant data.

The avian bornavirus workstream is described at a research-governance and evidence-analysis level. Any laboratory work must occur through appropriately qualified and authorised collaborators under applicable biosafety, veterinary, welfare, and regulatory controls.

## Use of Claude Science and other AI systems

AI systems may assist with literature mapping, code drafting, data-quality checks, statistical exploration, figure preparation, and manuscript editing. They are not treated as authors, veterinarians, laboratory supervisors, or sources of truth.

Every AI-assisted output must be checked against primary sources, validated by a competent human, and disclosed where required. See [`docs/AI_USE_AND_VALIDATION.md`](docs/AI_USE_AND_VALIDATION.md).

## Publication model

Outputs may be released in stages:

1. protocol or schema pre-release;
2. de-identified dataset or aggregate table;
3. executable analysis notebook;
4. preprint or conference material;
5. peer-reviewed article;
6. corrected or expanded version.

Each release should include:

- a version identifier;
- a clear data cutoff;
- inclusion and exclusion criteria;
- a provenance statement;
- a limitations section;
- code and dependency information;
- citation instructions;
- and a contact route for corrections.

## How to contribute

Contributions are welcome when they improve scientific clarity, animal welfare, reproducibility, accessibility, or data quality.

Useful contributions include:

- corrections to outcome definitions;
- validation rules for avian breeding and clinical data;
- statistical-review comments;
- species-neutral metadata improvements;
- documentation and accessibility improvements;
- test cases for the analysis code;
- literature references supporting or challenging a protocol.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening an issue or pull request.

## Citation

Use the repository citation metadata in [`CITATION.cff`](CITATION.cff). When citing a specific dataset, notebook, protocol, or release, cite that version rather than only the repository landing page.

## Licensing

- Code is released under the Apache License 2.0.
- Original documentation and synthetic demonstration data are released under Creative Commons Attribution 4.0 International.
- Third-party material remains subject to its original licence and must be attributed separately.

See [`LICENSE.md`](LICENSE.md).

## Disclaimer

This repository is for research, education, documentation, and reproducibility. It is not a substitute for examination by an avian veterinarian, formal ethics review, diagnostic-laboratory quality systems, statutory permissions, or species-specific professional judgement.

## Project leads

- **Dr. Debashis Banerjee**
- **Dr. Anindita Banerjee**

## Contact

**Sunshine BirdWorld**  
Rural West Bengal, India  
Email: [info@sunshinebirdworld.org](mailto:info@sunshinebirdworld.org)  
Website: [https://www.sunshinebirdworld.org](https://www.sunshinebirdworld.org)  
GitHub: [https://github.com/sunshinebirdworld/avian-research](https://github.com/sunshinebirdworld/avian-research)  
GitLab mirror: [https://gitlab.com/sunshinebirdworld/avian-research](https://gitlab.com/sunshinebirdworld/avian-research)
