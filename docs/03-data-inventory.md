# 3. Data Inventory

> Note: a real version of this document would include a data-flow diagram. This project's `README.md` flags that as a suggested next addition — it's genuinely useful to draw once the categories below are agreed, but the categories themselves are the governance-relevant artifact.

| Data element | Collected? | Why collected | Owner | Who can access |
|---|---|---|---|---|
| User query text (the question typed/spoken) | Yes | Needed to generate a response; needed in aggregate to improve the knowledge base | a2i / hosting ministry (system operator) | Chatbot service (automated), operations team (aggregated/anonymised only) |
| Session metadata (timestamp, channel used — web/SMS/WhatsApp, language selected) | Yes | Service analytics, load monitoring, channel-equity reporting (are rural/SMS users getting equal service?) | System operator | Operations team, M&E (monitoring & evaluation) team |
| Phone number (if using SMS/WhatsApp channel) | Yes, for that channel only | Required to deliver the reply on that channel | Telecom/SMS gateway processor on operator's behalf | Gateway system (automated); operator does not persist beyond session unless user opts into follow-up |
| NID number, date of birth, address, or other personal identifiers **if volunteered by the user in a query** | Incidentally, not by design | Users will sometimes paste their own NID number into a question ("why is my NID number 123... rejected?") | System operator | This is the single highest-risk data category in this inventory — see `05-privacy-risks.md` |
| Human-agent handoff transcript | Yes, for escalated cases only | Continuity of service when a human takes over | 333 Helpline / relevant ministry call centre | Human agent handling the case, QA reviewer |
| Aggregated analytics (top query categories, resolution rate, escalation rate) | Yes | Service improvement, KPI reporting (see `09-kpi-dashboard.md`) | System operator | Operator management, published in de-identified form to a2i/ICT Division |
| Model feedback (thumbs up/down on an answer) | Yes, optional | Quality improvement, bias/error detection | System operator | Developers/QA team, in aggregate |

## What this system explicitly does **not** collect or store
- No integration with or copy of the NID database, land record registry, or safety-net beneficiary lists (see scope boundary in `01-problem-definition.md`).
- No biometric data.
- No persistent user profile linking a phone number to a query history beyond the operational retention window (see `07-governance-framework.md` for the retention policy).

## Ownership principle

Data ownership follows the **source of authority**, not the system that happens to process it. The chatbot operator is a *processor* of citizen queries, not the *owner* of any underlying civil registry, land, or NID data — even when a citizen mentions such data in a query. This distinction matters legally and is the basis for the access-control rules in `07-governance-framework.md`.

## Access principle

Access is **role-based and purpose-limited**: nobody gets "all data" access by default. A support agent handling an escalation sees only that one transcript; an analytics team sees only aggregated, de-identified data; a developer debugging the model sees synthetic/sampled data with personal identifiers redacted wherever technically feasible.
