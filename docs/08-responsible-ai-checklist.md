# 8. Responsible-AI Checklist

Organised by lifecycle stage. Each item traces back to a risk in `06-ai-risks.md` or a control in `07-governance-framework.md` — this isn't a generic checklist, it's this project's risk analysis turned into gates.

## Before design sign-off
- [ ] Scope boundary documented and agreed by System Owner (`01-problem-definition.md`) — what the bot will *not* do is as clearly agreed as what it will.
- [ ] Data inventory and classification completed and reviewed by Data Protection Lead (`03`, `04`).
- [ ] Roles assigned for System Owner, Data Protection Lead, Technical Lead, Curator, and QA/Bias Reviewer — with segregation of duties confirmed.

## Before each release (including v1 launch)
- [ ] Answers are retrieval-grounded against the approved knowledge base; open-ended generation without a source is disabled or clearly flagged as unverified.
- [ ] Dialect/register/literacy-diversity test set run, with disaggregated results reviewed — not just an aggregate accuracy score (bias risk). A real 10-dialect Bangla corpus is wired into `demo/tests/` — see `11-real-data-sources.md`.
- [ ] Adversarial test queries run for known-sensitive/discriminatory patterns (discrimination risk).
- [ ] Prompt-injection and abuse test cases run (security risk). A real, labelled Bengali smishing dataset is available for testing SMS-channel phishing-pattern detection — see `11-real-data-sources.md`.
- [ ] PII detection/redaction pipeline tested against realistic sample queries containing NID-like numbers, phone numbers, addresses (privacy risk).
- [ ] Every escalation/fallback path logs a reason code (explainability).
- [ ] Retention rules from `07-governance-framework.md` implemented and verified, not just documented.
- [ ] Incident response contacts and escalation authority (who can pull the system down) confirmed and reachable.
- [ ] Plain-language privacy notice available, including a spoken/audio version for the voice/SMS channel.
- [ ] QA/Bias Reviewer sign-off obtained and recorded — independent of the development team.

## Ongoing (monthly/quarterly cadence)
- [ ] KPI dashboard reviewed (`09-kpi-dashboard.md`) — including equity-disaggregated metrics, not just overall volume/satisfaction.
- [ ] Random-sample human review of bot answers conducted (human oversight).
- [ ] Knowledge-base freshness check run; stale entries flagged to Curator.
- [ ] Incident log reviewed for patterns by the oversight body.
- [ ] Access logs to Confidential/Sensitive data reviewed by Data Protection Lead.
- [ ] Any proposed new data use or scope change formally logged and reviewed against `01` and `04` before implementation (anti function-creep control).

## Before any scope expansion (e.g. adding a transactional capability, integrating a live database)
- [ ] This is treated as a new project for governance purposes, not an incremental update — full re-run of the above from design sign-off, because the risk profile changes qualitatively, not just quantitatively.
