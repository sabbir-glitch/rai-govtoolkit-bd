# 11. Real Data Sources & Provenance

This toolkit's core documents (`01`–`10`) use illustrative content by design — a pilot team would need institutional authority to use real citizen data. But four real, publicly available datasets (sourced via Kaggle) can meaningfully strengthen specific parts of the toolkit: grounding the bias/dialect testing with real linguistic variation, grounding the security risk with a real phishing-pattern dataset, and grounding the KPI dashboard's aggregation thresholds with real population data. This document is itself a governance artifact — a data-source provenance register, which is exactly the kind of record `07-governance-framework.md` calls for under "Data quality."

## 1. Dialect Based Bangla Language dataset

| Field | Value |
|---|---|
| **Source** | Kaggle — `koushikrudra/bleach-clean-dataset` |
| **License** | Apache 2.0 |
| **Content** | Bengali text labelled across 10 major regional dialects, with `text`, `dialect`, and `text_length` columns, split into train/val/test |
| **Used for** | Replacing the hand-written 3-sentence informal-phrasing test in `demo/tests/test_governance_checks.py` with a real, larger dialect-robustness evaluation set |
| **Referenced in** | `06-ai-risks.md` (Bias), `08-responsible-ai-checklist.md` |
| **Limitation** | A single contributor's dataset, not an institutionally validated linguistic corpus. Good for expanding test coverage; not a substitute for a proper linguistic review by Bangla NLP specialists before a real deployment. |

## 2. Bengali SMS Smishing Dataset

| Field | Value |
|---|---|
| **Source** | Kaggle — `mdferozahmedafm/bengali-sms-smishing-dataset` |
| **License** | MIT |
| **Content** | 7,005 labelled SMS messages (`smish` / `promo` / `normal`) across Bengali, English, Banglish, and code-mixed text, purpose-built for smishing/phishing detection research |
| **Used for** | Grounding the Security risk category with a real, purpose-built adversarial dataset — directly relevant since Seba Bondhu's SMS channel is named in `05-privacy-risks.md` as a phishing-impersonation risk |
| **Referenced in** | `06-ai-risks.md` (Security) |
| **Limitation** | The dataset's own documentation notes it's a research resource, not a full representation of real-world SMS traffic, and that new phishing campaigns may not be represented. Treat as a starting evaluation set, not a complete defence. |

## 3. Bangladesh Districts wise population

| Field | Value |
|---|---|
| **Source** | Kaggle — `msjahid/bangladesh-districts-wise-population` |
| **License** | Apache 2.0 |
| **Content** | City/district population figures for 1991–2022, with administrative division, scraped from citypopulation.de and Wikipedia's Districts of Bangladesh |
| **Used for** | Real denominators for the minimum-aggregation-threshold privacy rule in `05-privacy-risks.md` ("don't publish a statistic representing fewer than a set number of users") and for district-level equity reporting in `09-kpi-dashboard.md` |
| **Referenced in** | `09-kpi-dashboard.md` |
| **Limitation** | Scraped secondary-source data, not an official BBS (Bangladesh Bureau of Statistics) census extract — fine for illustrative KPI-threshold calibration, not authoritative for policy decisions. |

## 4. Mobile network coverage (Upazila-level)

| Field | Value |
|---|---|
| **Source** | Kaggle — `mushfiqurrobin/network-coverage` |
| **License** | "Data files © Original Authors" — **not openly licensed**; do not redistribute this data or a derivative of it |
| **Content** | Upazila/Thana-level mobile operator coverage and self-reported satisfaction scores across Bangladesh |
| **Used for** | Contextual reference only, for reasoning about where the equity KPI ("resolution rate by channel: web vs SMS vs WhatsApp") is likely to matter most |
| **Referenced in** | `09-kpi-dashboard.md`, cited but not included |
| **Limitation** | Self-collected by a single individual in 2021 using the Opensignal app as a proxy — not an operator-verified or current dataset, and its license does not permit redistribution. Cite the source and methodology; do not treat its numbers as ground truth, and do not copy the data itself into this or any derived repository. |

## How to actually pull these in (rather than vendoring copies)

Two of these (dialect, smishing) are permissively licensed and small enough to be useful as real test-set inputs. Rather than committing a static copy into this repo — which risks going stale and duplicates data the source already hosts — `demo/scripts/fetch_kaggle_testsets.py` downloads them on demand via the Kaggle API when a developer has their own Kaggle credentials configured. See `demo/README.md` for setup.
