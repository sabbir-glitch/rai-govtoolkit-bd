# 7. Governance Framework

## Roles and responsibilities

| Role | Held by (example) | Responsibilities |
|---|---|---|
| **System Owner** | Designated official within the hosting ministry / a2i | Final accountability for the system; approves any scope change against `01-problem-definition.md`; reports to oversight body. |
| **Data Protection Lead** | Named data administrator, not the same person as System Owner | Owns the data inventory and classification (`03`, `04`); approves any new data use; leads incident response. |
| **Technical Lead** | Development team lead | Owns model/retrieval architecture, security controls, and the responsible-AI checklist (`08`) at each release. |
| **Content/Knowledge-Base Curator** | Subject-matter staff from relevant ministries | Owns accuracy and currency of the source documents the bot retrieves from — the single most important control against hallucination. |
| **QA / Bias Reviewer** | Independent from the dev team (rotating or external) | Runs the dialect/discrimination test suite in `06-ai-risks.md` before each release; can block a release. |
| **Human Escalation Agents** | 333 Helpline / UDC staff | Handle escalated queries; flag systemic bot errors back to the Technical Lead and Curator. |
| **Oversight body** | An inter-ministerial digital-governance committee (or equivalent existing body under ICT Division) | Periodic (e.g. quarterly) review of KPIs (`09`), incident reports, and any scope-change requests. |

## Access controls

- **Role-based, least-privilege by default** — see the access column in `03-data-inventory.md` for the concrete mapping.
- **Segregation of duties**: the person who curates content is not the same person who has raw log access; the Data Protection Lead is organisationally separate from the Technical Lead so data-use approval isn't self-granted.
- **Logged access**: every access to Confidential or Sensitive-tier data is itself logged (who, when, what record) — this log is reviewed by the Data Protection Lead, not just generated and forgotten.
- **No standing "admin sees everything" account** for routine operations; break-glass access for genuine emergencies is logged and reviewed after the fact.

## Retention

| Data tier | Retention | Rationale |
|---|---|---|
| Public (knowledge-base content) | Indefinite, version-controlled | It's the operational asset; old versions kept for audit trail of what the bot "knew" at a given time. |
| Internal (aggregated analytics) | 24 months, then archived in aggregate-only form | Enough for year-over-year trend reporting without indefinite raw retention. |
| Confidential (raw session logs, handoff transcripts) | 90 days, then deleted or irreversibly de-identified | Enough window for QA, dispute resolution, and incident investigation; not indefinite. |
| Sensitive (any personal identifier captured incidentally) | Deleted on detection, target within 30 days maximum if not caught at ingestion | This is the tier retention policy is strictest about, by design — see `04-data-classification.md`. |

`[TBD — pilot decision]`: exact retention numbers above are a reasonable starting proposal, not a legally settled figure — a real deployment would set these in consultation with the Data Protection Lead and against whatever retention rules apply under Bangladesh's data protection framework once finalised.

## Data quality

- Knowledge-base content changes go through the Curator role with a named source (circular number, official notice) — no undocumented edits.
- A "content freshness" check: any knowledge-base entry not reviewed within a defined period (e.g. 6 months) is flagged for re-verification, since government fee/document requirements do change.
- Model output quality tracked continuously via the KPIs in `09-kpi-dashboard.md`, not just at initial launch.

## Incident response

1. **Detect**: automated monitoring flags anomalies (spike in escalations, security-filter triggers, a QA-flagged bad answer going viral/complained-about).
2. **Contain**: Technical Lead has authority to disable a specific answer/knowledge-base entry or, in a severe case, the whole channel, without waiting for a full committee sign-off.
3. **Assess**: Data Protection Lead determines if any personal data was exposed; if so, this becomes a data-breach process, not just a bug-fix process.
4. **Notify**: System Owner informs the oversight body; if personal data was exposed, affected citizens are notified through the clearest available channel, in plain Bangla.
5. **Remediate & document**: root-cause fix, and a written incident report added to a running log reviewed quarterly by the oversight body — patterns across incidents matter as much as any single one.

## Human oversight

- The bot's role is strictly **informational and navigational**, never determinative (see scope boundary in `01`) — this is itself the primary human-oversight control, because it means no citizen's actual entitlement or record is ever changed by the AI alone.
- Every escalation path leads to a human who can override, correct, or take responsibility for a decision — the bot is never the last word on an ambiguous or high-stakes query.
- Periodic human sampling review of a random slice of bot answers (not just user-flagged ones), because users under-report bad answers they don't recognise as wrong.
