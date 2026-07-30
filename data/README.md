# Breeding event demonstration data

> ## Experimental Demonstration Repository
>
> This is an early stage, nonproduction demonstration of proposed research methods, schemas, synthetic data and analysis workflows. It does not contain validated Sunshine BirdWorld research findings unless expressly stated. Sunshine BirdWorld’s substantive scientific work is ordinarily communicated through peer reviewed journals, veterinary and avicultural publications, books, conferences and established scientific forums. The material must not be used for veterinary, clinical, husbandry, conservation, legal or regulatory decisions without independent expert review. Sensitive operational information is intentionally excluded.

## Important disclaimer

`example_breeding_events.csv` is **synthetic demonstration data**. It is generated to exercise schemas, validation rules, and analysis code. It must **not** be represented as real Sunshine BirdWorld institutional breeding results, clinical outcomes, or conservation performance.

For genuine scientific correspondence: [info@sunshinebirdworld.org](mailto:info@sunshinebirdworld.org) · [https://www.sunshinebirdworld.org](https://www.sunshinebirdworld.org)  
Principal investigators: Drs Debashis & Anindita Banerjee.

## Contents

| File | Description |
|---|---|
| `example_breeding_events.csv` | 160 synthetic egg records across 4 species (40 eggs each): *Ara chloropterus*, *Cacatua moluccensis*, *Probosciger aterrimus*, *Eclectus roratus*. |

## Columns (brief)

| Column | Meaning |
|---|---|
| `egg_id` | Unique egg identifier |
| `clutch_id` | Parent clutch |
| `pair_id` | Parent breeding pair |
| `species_scientific` / `species_common` | Species names |
| `lay_date` | Lay date (ISO) |
| `season` | Analysis season stratum |
| `incubation_method` | `parental`, `artificial`, `mixed`, or `unknown` |
| `initial_weight_g` | First standardised egg weight (g) |
| `fertility_status` | `fertile`, `infertile`, `unknown`, or `not_assessed` |
| `embryo_loss_stage` | Loss stage or `none` / `not_applicable` / `unknown` |
| `hatch_status` | `hatched`, `not_hatched`, or `unknown` |
| `hatch_date` | Hatch date when hatched |
| `hatch_assistance` | Assistance level |
| `chick_id` | Chick identifier when assigned |
| `chick_status_day7` | Day-7 status |
| `data_quality_flag` | `ok`, `review`, or `exclude` |
| `source_record_type` | Provenance class |
| `verified_status` | Verification level |

Full field definitions, allowed values, logical validation rules, and derived metric formulae are in [`DATA_DICTIONARY.md`](../DATA_DICTIONARY.md) (§6 Egg and hatch table; §13 Core derived metrics).
