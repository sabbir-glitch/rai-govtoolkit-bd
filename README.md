# Responsible AI & Data Governance Toolkit
### Use case: *Seba Bondhu* — an AI-assisted citizen-service chatbot for Bangladesh

> **Status:** Portfolio / research project. Not an official government document. Built to demonstrate applied thinking in AI governance, data protection, and public-sector digital service design in a Bangladesh context.

## Why this project exists

Bangladesh's digital government push (a2i / "Aspire to Innovate", Union Digital Centres, the 333 National Helpline, e-Porjoy, myGov) has made huge progress connecting citizens to services. The natural next step many countries are taking is an AI-assisted chatbot layer on top of these services — answering questions about birth registration, NID (National ID) correction, land records, trade licences, and social safety-net programmes in Bangla and English, 24/7.

That next step also introduces real risk: hallucinated answers about legal entitlements, biased service quality across dialects/literacy levels, and handling of sensitive citizen data (NID numbers, addresses, family data) without a mature legal or institutional data-protection regime yet in place in Bangladesh.

This toolkit is a template for how such a system *should* be governed — from problem definition through to a public-facing policy brief — so that responsible AI isn't bolted on after deployment, but designed in from day one.

## Repo structure

| File | Contents |
|---|---|
| `docs/01-problem-definition.md` | The public-service problem, target users, scope, and what "success" means |
| `docs/02-stakeholder-map.md` | Government, citizens, developers, data administrators, vulnerable groups — and their stakes |
| `docs/03-data-inventory.md` | What data is collected, why, who owns it, who can access it |
| `docs/04-data-classification.md` | Public / Internal / Confidential / Sensitive labelling of every data element |
| `docs/05-privacy-risks.md` | What could go wrong, and for whom |
| `docs/06-ai-risks.md` | Bias, hallucination, discrimination, privacy, security, explainability |
| `docs/07-governance-framework.md` | Roles, responsibilities, access controls, retention, data quality, incident response, human oversight |
| `docs/08-responsible-ai-checklist.md` | Pre-launch and ongoing checklist, mapped to the risks above |
| `docs/09-kpi-dashboard.md` | Metrics to actually monitor this in production, with a mock dashboard spec |
| `docs/10-policy-brief.md` | 2–3 page plain-language brief for a non-technical decision-maker |
| `demo/` | A small, runnable chatbot implementing the key mitigations from `docs/06-ai-risks.md` and `docs/05-privacy-risks.md` — see `demo/README.md` |
| `docs/11-real-data-sources.md` | Provenance register for real datasets (Kaggle-sourced) used to strengthen the bias, security, and KPI-threshold parts of this toolkit |

## How to use this repo

1. Read `01` → `10` in order — each builds on the one before it.
2. Treat every `[TBD — pilot decision]` marker as a real open question a pilot team would need to resolve; they're left in deliberately rather than invented, because real governance decisions (e.g. exact retention periods, which ministry owns the data) require institutional authority this project doesn't have.
3. Fork/adapt the templates in `04`, `06`, and `08` for a different public-service AI use case — they're written to generalise beyond the chatbot example.

## Suggested next steps for this repo

- Add a `diagrams/` folder with an architecture + data-flow diagram (see note in `03-data-inventory.md`).
- Turn `08-responsible-ai-checklist.md` into a GitHub Issues template so each checklist item becomes a trackable task.
- Add a `CONTRIBUTING.md` if you want to open this up for feedback from others also targeting AI-governance / public-policy portfolio work.

## License

MIT for the templates and code structure. The policy brief and written analysis are original work — reuse with attribution.
