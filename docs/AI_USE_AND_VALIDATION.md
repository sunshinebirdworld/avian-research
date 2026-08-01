# AI Use and Human Validation

**Version:** 0.1.0  
**Effective date:** 2026-07-30  
**Contact:** info@sunshinebirdworld.org  
**Website:** https://www.sunshinebirdworld.org  
**Project leads:** Dr. Debashis Banerjee and Dr. Anindita Banerjee

## 1. Purpose

This policy defines how AI systems may assist Sunshine BirdWorld research work and what human verification is required before any AI-assisted material is treated as scientifically usable, publicly releasable, or clinically relevant.

AI systems are tools. They are not authors, veterinarians, laboratory supervisors, ethics committees, or sources of truth.

## 2. Permitted AI assistance

AI systems may help with:

- literature discovery and evidence mapping;
- drafting code, tests, and documentation;
- checking schema consistency and data-quality rules;
- exploratory statistical analysis;
- figure and table preparation;
- manuscript language editing;
- identifying alternative explanations or missing limitations;
- summarising repository structure for contributors.

## 3. Prohibited AI uses

AI systems must not independently:

- approve clinical treatment or animal disposition;
- certify diagnostic laboratory results;
- invent citations, datasets, assay results, or missing values;
- conceal uncertainty, exclusions, or negative findings;
- authorise release of restricted or identifiable records;
- be listed as an author;
- generate pathogen-enhancement, culture-optimisation, genetic-modification, or gain-of-function instructions for inclusion in this repository.

## 4. Mandatory human verification

Before relying on or publishing an AI-assisted output, a competent human must verify:

1. **Primary sources** — claims cite real, relevant sources that support the statement made.
2. **Data integrity** — numbers, denominators, exclusions, and units match the source tables.
3. **Method fit** — the statistical or analytical method matches the design and sample size.
4. **Domain sense** — avian biology, welfare, biosafety, and regulatory boundaries are respected.
5. **Disclosure** — AI assistance is disclosed where journals, funders, or institutional policy require it.
6. **Synthetic labelling** — demonstration or synthetic results are never presented as institutional Sunshine BirdWorld outcomes.

## 5. Risk tiers

### Tier 1 — Low risk (still review)

Spelling, formatting, repository navigation help, and boilerplate documentation edits.

### Tier 2 — Medium risk (domain review required)

Protocol drafting, schema changes, exploratory analysis, figure generation, and literature summaries.

### Tier 3 — High risk (named human sign-off required)

Anything affecting animal care decisions, diagnostic interpretation, public scientific claims, de-identification decisions, or release of real institutional data.

High-risk outputs require review by an appropriate professional role (for example avian veterinarian, data steward, or project lead) before use.

## 6. Documentation of AI assistance

For medium- and high-risk workstreams, retain:

- the task the AI was asked to perform;
- the model or system used, when known;
- the human reviewer;
- the verification steps performed;
- residual uncertainties.

## 7. Repository-specific rule for this release

The demonstration notebook and synthetic dataset in this repository were prepared to show an executable workflow. Their numeric results are **not** Sunshine BirdWorld institutional results. Any AI-generated commentary about those numbers must preserve that distinction.

## 8. Corrections

If an AI-assisted error enters a public release, correct it transparently with version history preserved and notify [info@sunshinebirdworld.org](mailto:info@sunshinebirdworld.org).
