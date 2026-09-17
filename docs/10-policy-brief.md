# Policy Brief: Responsible Deployment of an AI-Assisted Citizen-Service Chatbot

**Prepared as a governance proposal for a pilot public-service AI system ("Seba Bondhu")**
**Audience: Non-technical decision-makers — ministry leadership, digital-governance committee members**

---

## The opportunity, in one paragraph

Bangladeshi citizens frequently struggle to find clear, consistent answers to routine questions about government services — correcting an ID document, registering a birth, checking a land record, or understanding eligibility for a support programme. An AI-assisted chatbot, reachable by web, SMS, and WhatsApp, could answer these questions instantly, in Bangla, at any hour, and reduce the burden on the 333 National Helpline and local offices. Done well, this closes an access gap. Done carelessly, it creates a new one — and a new category of risk around citizens' personal data.

## What we're proposing

A pilot chatbot, **Seba Bondhu**, that is deliberately limited in scope at launch: it answers questions and directs citizens to the right office or portal, but it does not submit applications, process payments, or touch the National ID (NID) database or any other system of record. This narrow scope is a governance choice, not a technical limitation — it removes an entire category of risk while the institutional processes to manage a higher-risk version are still being built.

## Why governance has to come first, not follow-up

Two things go wrong when AI systems are built first and governed later:

1. **Wrong answers cause real harm.** If the bot confidently tells a citizen the wrong document or deadline, that citizen may travel to the wrong office, miss a deadline, or lose trust in digital government services altogether — the opposite of the intended effect.
2. **The people the system is meant to help most are the easiest to underserve.** AI systems trained mostly on formal, urban language patterns tend to perform worse for rural dialects, informal spelling, and lower-literacy phrasing. Without deliberately testing for this, a well-intentioned system can end up working best for the citizens who already have the least difficulty accessing services — and worst for those it was meant to help.

The accompanying toolkit (this repository) works through both problems concretely: a full data inventory and classification, a six-category AI risk assessment (bias, hallucination, discrimination, privacy, security, explainability), and a governance framework defining exactly who is responsible for what.

## The core governance commitments

- **A named, separate Data Protection Lead** who is not the same person building the system — so data-use decisions aren't self-approved.
- **Every factual answer is grounded in an approved, sourced document** (an official circular or FAQ), not open-ended AI generation — this is the single biggest lever against the bot confidently stating something false.
- **Equity is a measured metric, not an assumption.** The system tracks whether it performs equally well across channels, dialects, and regions, and a widening gap in that data is treated as a release-blocking problem.
- **Strict data minimisation.** No integration with the NID database or other systems of record at launch; any personal information a citizen types into a query is automatically flagged, redacted from storage, and never used to further train the model.
- **A human is always reachable**, and the AI is never the final word on anything that affects a citizen's actual record or entitlement.
- **An incident response process exists before launch, not after the first incident** — including a plain-Bangla process for notifying affected citizens if something does go wrong.

## What this costs, in plain terms

Governance of this kind is not free: it requires a dedicated Data Protection Lead role, an independent QA/bias review before each release (separate from the development team), ongoing content curation by subject-matter staff, and a quarterly oversight review. This is a real, ongoing institutional commitment — not a one-time technical setup. The alternative cost — a public trust failure from a government-branded AI system giving citizens wrong information, or a data-handling incident — is larger and harder to recover from.

## What we're asking of decision-makers

1. **Approve the narrow initial scope** (informational and navigational only) as a deliberate first phase, with any expansion treated as a new governance review, not an incremental update.
2. **Designate the named roles** in the governance framework — particularly a Data Protection Lead independent from the technical team.
3. **Commit to the quarterly KPI and incident review cadence**, so this isn't a one-time approval but an ongoing oversight relationship.

## Bottom line

An AI chatbot can genuinely improve how Bangladeshi citizens access government services — but only if the system is built to be honest about what it doesn't know, equitable across the population it's meant to serve, and accountable when something goes wrong. This proposal treats those three properties as launch requirements, not future improvements.

---
*This brief accompanies a full governance toolkit covering problem definition, stakeholder mapping, data inventory and classification, privacy and AI risk analysis, the governance framework, a pre-launch checklist, and a KPI dashboard specification. See the repository README for the complete set of documents.*
