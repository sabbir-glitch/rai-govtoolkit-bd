# 5. Privacy Risks

For each risk: **what could go wrong**, **who it harms**, and **the mitigation this toolkit assumes**.

## 1. Citizens volunteering sensitive data in free-text queries
A citizen typing "my NID is 1990XXXXXXXX and it says my father's name is wrong, what do I do?" hands the system a national ID number unprompted. If that text is logged, stored, or later used to fine-tune a model, it becomes a persistent, hard-to-purge copy of a national identifier outside the systems legally responsible for protecting it.
- **Harm**: identity-fraud exposure; loss of citizen trust; potential legal liability for the operator.
- **Mitigation**: automated PII pattern detection (NID format, phone number format) at ingestion, redaction before storage, and a hard rule that raw query logs are never used as model training data (see `07-governance-framework.md`).

## 2. Re-identification from "anonymised" analytics
Aggregated data can still be re-identifying in a small-population slice — e.g. "the one user from a specific upazila who asked about a rare pension category this month" could be identifiable to someone with local knowledge.
- **Harm**: indirect exposure of a citizen's circumstances (e.g. applying for a disability allowance) even without a name attached.
- **Mitigation**: minimum aggregation thresholds (don't publish a statistic representing fewer than a set number of users/queries); geographic data reported at district level, not union/village level, in any public report.

## 3. SMS/WhatsApp channel data passing through a third-party gateway
The messaging channel that makes the bot accessible to low-bandwidth users also means a third-party telecom/platform provider handles the phone number and message content in transit.
- **Harm**: data leaving the operator's direct control, subject to a different (possibly foreign) jurisdiction's data practices.
- **Mitigation**: contractual data-processing terms with the gateway provider, minimal data passed (no persistent linkage of phone number to query history beyond the single session), documented in `03-data-inventory.md`.

## 4. Human-agent handoff exposing more than necessary
When a query escalates to a human (333 helpline or UDC staff), the agent may see the full conversation, including anything sensitive the citizen typed earlier in the session.
- **Harm**: unnecessary exposure of personal data to a human who only needed to answer a narrower question.
- **Mitigation**: handoff shares only the relevant recent turns, not the full session history, with a clear log of what was shared and to whom.

## 5. Function creep — "since we have this data, let's also..."
The most common way public-sector data systems drift out of their original privacy scope is incremental: a later administrator asks to link query data to the NID database "just for this one report," and each individual ask seems reasonable.
- **Harm**: gradual erosion of the scope boundary set in `01-problem-definition.md`, without any single decision-maker having approved the full extent of the change.
- **Mitigation**: any proposed new data use must be logged and reviewed against this document and re-classified per `04-data-classification.md` before implementation — not approved informally.

## 6. Vulnerable users and consent in practice
Many citizens using the bot — especially first-time digital users guided by a family member or UDC staff — may not meaningfully understand what happens to their query data, regardless of what a privacy notice says.
- **Harm**: "consent" that is technically obtained but not truly informed, especially for elderly or low-literacy users.
- **Mitigation**: a short, spoken/Bangla-audio privacy notice option for the SMS/voice channel, not just a text wall; a default of *not* storing anything beyond the operational retention window regardless of whether the user actively engages with a consent notice.
