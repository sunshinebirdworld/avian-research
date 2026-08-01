# Research Scope

## 1. Programme identity

**Programme name:** Sunshine BirdWorld Avian Research Methods  
**Institutional setting:** Managed avicultural breeding and research population in rural West Bengal, India  
**Primary purpose:** Non-commercial evidence generation for avian health, welfare, conservation breeding, disease surveillance, and reproducible avicultural science  
**Repository role:** Public methods, schemas, code, synthetic examples, and approved de-identified or aggregate outputs

## 2. Overarching research question

How can long-duration records from a managed, species-diverse avicultural population be converted into scientifically defensible and reproducible evidence that improves avian health, welfare, breeding outcomes, and conservation practice?

## 3. Specific aims

### Aim 1 — Standardise breeding and reproductive outcome data

Develop and maintain explicit definitions for:

- pairing and breeding exposure;
- clutch identity;
- egg fertility;
- embryo-development stage;
- embryo mortality;
- hatchability;
- assisted hatching;
- congenital or developmental abnormality;
- early chick survival;
- weaning outcome;
- parental versus artificial incubation and rearing.

Expected outputs include data dictionaries, validation rules, outcome tables, and species-stratified observational analyses.

### Aim 2 — Quantify incubation, hatching, and neonatal outcomes

Estimate and compare:

- fertility rate;
- overall hatch rate;
- hatchability of fertile eggs;
- stage-specific embryo loss;
- assistance rate;
- survival to prespecified neonatal time points;
- growth trajectories;
- associations with season, incubation method, clutch characteristics, parental history, and measured environmental conditions.

Analyses will use confidence intervals and explicit denominators. Small samples will not be presented as definitive evidence.

### Aim 3 — Build reproducible retrospective clinical evidence

Convert historical and prospective clinical observations into structured case records suitable for:

- descriptive case series;
- syndrome surveillance;
- diagnostic-yield analysis;
- treatment-response documentation;
- adverse-event review;
- hypothesis generation.

The programme does not replace prospective controlled trials when those are required. Retrospective records will be labelled as such.

### Aim 4 — Support responsible avian disease surveillance

Create harmonised metadata for:

- sample collection;
- specimen type;
- diagnostic target;
- assay platform;
- result interpretation;
- repeat testing;
- clinical status;
- epidemiological linkage;
- quality-control status.

Surveillance outputs will distinguish infection evidence, clinical disease, exposure, inconclusive findings, and untested assumptions.

### Aim 5 — Advance high-level avian bornavirus research

Investigate evidence relevant to avian bornavirus and proventricular dilatation disease, including:

- longitudinal clinical and diagnostic patterns;
- test-result concordance;
- association between detectable infection markers and clinical phenotype;
- sampling strategy and repeat-testing logic;
- immune-response questions relevant to DIVA-oriented research;
- candidate outcome measures for future collaborative studies.

This repository will not publish pathogen-enhancement methods, culture optimisation, genetic manipulation, or operational instructions that exceed an appropriate open scientific risk boundary. Laboratory studies must be performed by qualified and authorised collaborators under applicable biosafety, welfare, veterinary, and regulatory controls.

### Aim 6 — Evaluate husbandry, biosecurity, and environmental evidence

Study associations between recorded operational conditions and outcomes, including:

- temperature and humidity;
- incubation conditions;
- cleaning and disinfection events;
- enclosure or nursery zone;
- power or equipment interruptions;
- quarantine and movement status;
- density and cohort structure;
- season and extreme-weather periods.

Observational associations will not be described as causal without an appropriate design.

### Aim 7 — Develop reusable avicultural research infrastructure

Release reusable resources such as:

- variable definitions;
- controlled vocabularies;
- validation rules;
- de-identification procedures;
- reproducible notebooks;
- reporting templates;
- protocol checklists;
- machine-readable schemas;
- citation and correction practices.

## 4. Populations and units of analysis

Depending on the research question, the unit of analysis may be:

- individual bird;
- breeding pair;
- breeding exposure;
- clutch;
- egg;
- hatch event;
- chick;
- clinical episode;
- diagnostic sample;
- treatment course;
- enclosure or nursery zone;
- daily environmental interval;
- equipment or power event.

The unit must be stated before analysis. Eggs from the same clutch, repeated measures from the same bird, and birds from the same pair are not automatically statistically independent.

## 5. Data sources

Potential sources include:

- statutory or institutional animal registers;
- breeding and hatch records;
- incubator records;
- neonatal weight charts;
- veterinary examination notes;
- medication and treatment records;
- diagnostic laboratory reports;
- necropsy or pathology reports;
- environmental sensors;
- equipment logs;
- biosecurity and sanitation records;
- transfer or movement records;
- photographic records where ethically and legally appropriate;
- published literature and public reference datasets.

A source record is not assumed to be error-free. Data provenance and verification state must be preserved.

## 6. Primary outcome families

### Reproductive outcomes

- fertility status;
- early, middle, or late embryo loss;
- hatch status;
- hatch assistance;
- malposition;
- hatch abnormality;
- seven-day survival;
- 30-day survival;
- weaning survival;
- age at weaning.

### Clinical outcomes

- symptom resolution;
- partial response;
- non-response;
- recurrence;
- adverse event;
- death or euthanasia;
- time to event;
- diagnostic confirmation status.

### Surveillance outcomes

- positive, negative, inconclusive, invalid, or not tested;
- repeat-test concordance;
- conversion or reversion pattern;
- syndrome incidence;
- cluster detection;
- exposure classification.

### Operational outcomes

- environmental deviation;
- equipment interruption;
- power interruption;
- corrective-action time;
- protocol deviation;
- completeness of critical records.

## 7. Inclusion criteria

A record may be included when:

- the unit of analysis can be uniquely identified without public disclosure of sensitive identifiers;
- the relevant denominator can be established;
- the outcome definition is compatible with the study protocol;
- dates are sufficiently precise for the planned analysis;
- key provenance fields are available;
- duplicate records can be resolved;
- inclusion is lawful and consistent with welfare, privacy, and institutional obligations.

## 8. Exclusion criteria

A record may be excluded when:

- identity or event linkage cannot be resolved;
- the outcome is missing and cannot be responsibly classified;
- the record is a duplicate;
- dates are internally impossible;
- the animal or event falls outside the prespecified population;
- the source record is unreliable and cannot be independently checked;
- publication would create disproportionate privacy, welfare, security, or regulatory risk.

Exclusions must be counted and reported. Records should not be removed merely because they weaken a preferred conclusion.

## 9. Study-design hierarchy

The programme may include:

1. descriptive audits;
2. retrospective observational studies;
3. prospective observational cohorts;
4. diagnostic-accuracy studies;
5. interrupted time-series or before-and-after evaluations;
6. case-control analyses;
7. collaborative controlled studies where ethically and operationally appropriate.

The strength of a conclusion must match the design.

## 10. Statistical principles

- Prespecify primary outcomes and denominators.
- Report effect sizes and uncertainty, not only p-values.
- Use exact or Wilson intervals for small proportions where appropriate.
- Account for clustering by pair, clutch, enclosure, or individual when the design requires it.
- Treat repeated measures as repeated measures.
- Distinguish missing, not applicable, not performed, and unknown.
- Avoid species-level claims when the sample is too small.
- Do not pool biologically dissimilar species without justification.
- Separate exploratory from confirmatory analysis.
- Preserve negative and null results.
- Record all material analysis changes.

## 11. Data-quality objectives

Each released analysis should report:

- number of source records reviewed;
- number included and excluded;
- duplicate count;
- missingness by critical field;
- logical-validation failures;
- manual corrections;
- verification status;
- data cutoff;
- software and package versions.

Critical fields should target at least 95% completeness before formal analysis unless the research question explicitly concerns missingness.

## 12. Animal-welfare and ethics boundary

This programme is built around welfare improvement and responsible evidence generation.

Before release, each project must consider:

- whether the work changes animal handling or care;
- whether formal ethics or institutional review is required;
- whether sampling is clinically indicated, minimally invasive, or research-only;
- whether burden and benefit are proportionate;
- whether adverse events are captured;
- whether a stopping rule is required;
- whether the work could encourage unsafe replication.

No public protocol should be interpreted as authorising a procedure that requires a veterinarian, ethics committee, statutory permission, or biosafety oversight.

## 13. Privacy, security, and legal exclusions

The public repository excludes or transforms:

- human names and contact details;
- staff schedules and access credentials;
- exact enclosure maps;
- surveillance-camera positions;
- anti-poaching systems;
- private correspondence;
- legal-case materials unrelated to the scientific question;
- commercial transaction details;
- animal-transfer details that create security risk;
- precise location data beyond what is scientifically necessary.

## 14. Publication and peer-review plan

For each study:

1. freeze a versioned analysis dataset;
2. generate a machine-readable data dictionary;
3. run validation and missingness reports;
4. execute the notebook from a clean environment;
5. archive outputs and software versions;
6. obtain domain and statistical review;
7. release a protocol or analysis plan where feasible;
8. submit a manuscript, preprint, poster, or technical report;
9. link corrections and later versions.

## 15. AI-assisted research boundary

Claude Science and other AI systems may assist with:

- literature discovery and evidence mapping;
- drafting code and tests;
- checking schema consistency;
- exploratory analysis;
- figure and table preparation;
- manuscript language editing;
- identifying possible alternative explanations.

AI systems may not independently:

- approve clinical treatment;
- determine animal disposition;
- certify diagnostic results;
- replace a qualified statistician for high-stakes inference;
- fabricate citations or missing data;
- conceal uncertainty;
- be listed as an author.

Human verification requirements are documented in `docs/AI_USE_AND_VALIDATION.md`.

## 16. Current public deliverables

This initial release contains:

- a detailed research scope;
- a harmonised data dictionary;
- six operational research protocols;
- an executable breeding-outcomes notebook;
- a synthetic demonstration dataset;
- reusable Python functions for proportion estimates and validation.

## 17. Planned development

### Phase 1 — Foundation

- complete repository governance;
- validate terminology with avian veterinarians and breeders;
- add automated schema tests;
- create specimen and clinical-event templates.

### Phase 2 — Retrospective harmonisation

- map selected historical records;
- quantify missingness and bias;
- publish aggregate descriptive reports;
- identify questions suitable for formal manuscripts.

### Phase 3 — Prospective collection

- introduce standard prospective fields;
- improve denominator capture;
- add environmental and equipment-event linkage;
- preregister selected analyses where feasible.

### Phase 4 — Collaborative science

- invite external veterinary, diagnostic, statistical, and academic review;
- release de-identified datasets when lawful and responsible;
- submit peer-reviewed outputs;
- maintain corrections and long-term data stewardship.

## 18. Explicit non-claims

This programme does not claim that:

- all observational associations are causal;
- all species can be pooled;
- a single facility represents global aviculture;
- AI-generated analyses are automatically valid;
- a surveillance result alone establishes clinical disease;
- a synthetic demonstration dataset is real-world evidence;
- open publication removes the need for professional judgement.

The repository exists to make claims narrower, clearer, and more testable.
