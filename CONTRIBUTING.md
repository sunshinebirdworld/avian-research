# Contributing

Thank you for helping improve Sunshine BirdWorld Avian Research Methods.

Project leads: **Dr. Debashis Banerjee** and **Dr. Anindita Banerjee**  
Contact: [info@sunshinebirdworld.org](mailto:info@sunshinebirdworld.org)  
Website: [https://www.sunshinebirdworld.org](https://www.sunshinebirdworld.org)  
Repository: [https://github.com/sunshinebirdworld/avian-research](https://github.com/sunshinebirdworld/avian-research)

## What we welcome

- Corrections to outcome definitions and validation rules
- Improvements to schemas and controlled vocabularies
- Statistical-review comments and test cases
- Documentation and accessibility improvements
- Literature references that support or challenge a protocol
- Bug reports in analysis code or notebooks

## What we do not accept

- Real institutional records that have not passed the release checks in `protocols/P01_DATA_GOVERNANCE_AND_DEIDENTIFICATION.md`
- Names, phone numbers, addresses, staff identifiers, client data, or other personal information
- Exact enclosure maps, camera placement, access systems, or anti-poaching details
- Pathogen culture, propagation, genetic modification, or gain-of-function methods
- Unvalidated treatment directions intended for use without veterinary oversight
- Content that misrepresents the synthetic demonstration data as Sunshine BirdWorld results

## Before you start

1. Read [`README.md`](README.md), [`RESEARCH_SCOPE.md`](RESEARCH_SCOPE.md), and [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md).
2. Read the relevant protocol under [`protocols/`](protocols/).
3. Read [`docs/AI_USE_AND_VALIDATION.md`](docs/AI_USE_AND_VALIDATION.md) if AI tools assisted your contribution.
4. Open an issue describing the proposed change before large redesigns.

## How to contribute

1. Fork the repository and create a focused branch.
2. Keep changes small and reviewable.
3. Update documentation when behaviour or definitions change.
4. For code changes, add or update checks where practical and re-run the demonstration notebook.
5. Open a pull request with:
   - a clear summary of the scientific or technical reason for the change;
   - any effect on historical analyses or field definitions;
   - confirmation that no restricted or identifiable data are included.

## Coding and analysis conventions

- Prefer clear, testable functions over opaque notebooks.
- Preserve denominators whenever rates or proportions are reported.
- Use Wilson or other appropriate interval methods for small proportions.
- Label synthetic outputs as synthetic in tables, figures, and prose.
- Do not invent missing data.

## Licensing

- Code contributions are accepted under the Apache License 2.0.
- Documentation contributions are accepted under Creative Commons Attribution 4.0 International.
- By contributing, you confirm you have the right to offer the material under those terms.

## Conduct

Be precise, civil, and evidence-oriented. Disagreement about methods is welcome; personal attacks and unsafe content are not.
