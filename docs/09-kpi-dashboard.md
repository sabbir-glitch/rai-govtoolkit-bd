# 9. KPI Dashboard

A dashboard spec, not just a metric list — grouped by what question each metric answers, since a KPI dashboard that's just a wall of numbers doesn't actually drive governance decisions.

## "Is it working?" — Service effectiveness
| KPI | Definition | Target direction |
|---|---|---|
| Query resolution rate | % of informational queries resolved without human escalation | Increase, but never at the cost of accuracy (see below) |
| Median time-to-answer | Seconds from query to response | Decrease |
| Escalation rate | % of sessions handed to a human agent | Track, don't just minimise — a healthy escalation rate for ambiguous/high-stakes queries is a *feature*, not a failure |
| User-reported helpfulness (thumbs up/down) | % positive feedback among rated responses | Increase |

## "Is it working equally well for everyone?" — Equity (the metrics this toolkit treats as non-optional)
| KPI | Definition | Target direction |
|---|---|---|
| Resolution rate by channel | Web vs. SMS vs. WhatsApp | Parity across channels |
| Resolution rate by language/dialect cluster (where inferable) | e.g. standard Bangla vs. regional-dialect-heavy queries | Parity — a widening gap here is a release-blocking signal, not a footnote |
| Escalation rate by region (district-level, aggregated per `04-data-classification.md` thresholds) | Are some regions escalating far more than others? | Investigate any large deviation, don't just report it |

Real district-level population figures (see `11-real-data-sources.md`) can calibrate the minimum-aggregation threshold referenced above — e.g. setting the threshold relative to a district's actual population rather than picking an arbitrary number. Mobile network coverage data can also inform *where* the channel-parity KPI is likely to matter most, though that particular source is not openly licensed and should be cited as context, not redistributed or treated as verified ground truth.

## "Is it safe and trustworthy?" — Risk (mapped to `06-ai-risks.md`)
| KPI | Definition | Target direction |
|---|---|---|
| Hallucination flag rate | % of sampled answers found factually incorrect in human review | Decrease toward near-zero; this is the most safety-critical single number on the dashboard |
| Security-filter trigger rate | Injection/abuse attempts blocked | Monitor for spikes (possible targeted attack) |
| PII-in-query detection rate | How often users volunteer sensitive data in free text | Informs whether the redaction pipeline and user-facing warnings need strengthening |
| Data-access log anomalies | Any access outside expected role/purpose pattern | Zero-tolerance; any instance triggers `07-governance-framework.md` incident response |

## "Is governance actually happening?" — Process health (often the first thing that quietly lapses)
| KPI | Definition | Target direction |
|---|---|---|
| Checklist completion rate | % of `08-responsible-ai-checklist.md` items completed and signed off per release | 100% before release, tracked historically |
| Knowledge-base freshness | % of content reviewed within the defined freshness window | Increase toward 100% |
| Incident response time | Time from detection to containment for logged incidents | Decrease |

## Suggested dashboard layout (for a future implementation)

A single-screen view with four quadrants matching the four groupings above, each with a simple trend line and a red/amber/green status against target — deliberately not more than ~12 numbers on the primary view, so it stays something an oversight committee actually looks at each quarter, with a drill-down available for the detail underneath.
