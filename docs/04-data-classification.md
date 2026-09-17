# 4. Data Classification

Four-tier scheme: **Public / Internal / Confidential / Sensitive**. Every element from `03-data-inventory.md` is classified below, with the handling rule that follows from the label.

| Data element | Classification | Handling rule |
|---|---|---|
| Published FAQ/knowledge-base content (service rules, required documents) | **Public** | Freely shareable; this is the content the bot is built on and is already public information. |
| Aggregated, de-identified analytics (query volume by category, resolution rate) | **Internal** | Shared within operator + a2i/ICT Division; may be published in reports without further review. |
| Raw session logs / query text (not yet reviewed for personal data) | **Confidential** | Access limited to operations and QA roles; not shared externally; time-limited retention. |
| Human-agent handoff transcripts | **Confidential** | Same as above, plus: only the assigned agent and a QA reviewer may access a given transcript. |
| Phone numbers (SMS/WhatsApp channel) | **Sensitive** | Processed only by the messaging gateway for delivery; not persisted in analytics stores; not linkable to query content beyond the single session. |
| Any NID number, DOB, address, or family data volunteered inside a query | **Sensitive** | Treated as personal data regardless of how it entered the system. Automated redaction attempted at ingestion (see `05-privacy-risks.md`); flagged for priority deletion; never used in model fine-tuning or shared in raw form for any purpose, including "improving the bot." |

## Classification rules of thumb used above

1. **Default to the higher tier when in doubt.** A query that *might* contain personal data is treated as if it does until reviewed, not the reverse.
2. **Aggregation can lower a tier; individual records rarely can.** Turning 10,000 raw queries into "62% of queries were about NID correction" is what moves data from Confidential to Internal — the raw queries themselves stay Confidential.
3. **A field's classification travels with it**, even into logs, backups, model training data, or a developer's local debugging environment. "It's just a log file" is not an exemption.
4. **Sensitive data gets the shortest retention window and the smallest access list of any tier**, by construction (see `07-governance-framework.md`).
