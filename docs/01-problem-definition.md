# 1. Problem Definition

## The problem

Millions of Bangladeshi citizens need routine information from government services — how to correct a National ID (NID), register a birth, check land record (khatian) status, apply for a trade licence, or find out eligibility for a social safety-net programme (e.g. Old Age Allowance, Vulnerable Group Feeding). Today this information is scattered across ministry websites, Union Digital Centre (UDC) staff knowledge, the 333 National Helpline call agents, and word of mouth.

Consequences of the current state:
- **Unequal access**: citizens in rural areas or without a nearby UDC rely on informal/paid intermediaries ("dalals") to navigate paperwork.
- **Call-centre bottleneck**: the 333 helpline is voice-only and has limited hours and agent capacity.
- **Inconsistent answers**: different agents or offices give different guidance for the same query.
- **Low digital literacy friction**: existing e-service portals assume a level of form-filling literacy many citizens don't have.

## Proposed intervention: *Seba Bondhu* ("Service Friend")

An AI-assisted chatbot (web + SMS/WhatsApp channel for low-bandwidth access) that:
1. Answers procedural questions about government services in Bangla and English ("What documents do I need to correct my date of birth on my NID?").
2. Guides users step-by-step to the correct official portal, office, or UDC — it **does not** perform the transaction itself.
3. Escalates to a human agent (333 helpline or UDC staff) when a query is ambiguous, high-stakes, or the user requests it.
4. Is built on top of authoritative source documents (ministry circulars, official FAQs) rather than open-web knowledge, to reduce hallucination risk.

## Explicit scope boundaries

**In scope:**
- Informational guidance on NID correction, birth/death registration, land record checks, trade licence application, and 3–5 major social safety-net programmes.
- Bangla (primary) and English.
- Human handoff pathway.

**Out of scope (deliberately, for this version):**
- The bot does **not** submit applications, make payments, or modify any government record.
- The bot does **not** make eligibility determinations for safety-net programmes — it explains criteria and directs the citizen to apply.
- No integration with the NID database or other systems of record in v1 — this removes an entire category of privacy/security risk until governance is proven out.

## Why this counts as a "public-service problem" and not just a tech demo

The problem is access and equity, not the absence of a chatbot. A chatbot is one possible intervention; this toolkit exists because *how* it's governed determines whether it closes the access gap or creates a new one (e.g. citizens trusting a wrong AI answer over a human, or the system quietly working better for literate urban users than for others).

## Success criteria (draft — a real pilot would validate these)

- Reduction in "wrong information" complaints compared to informal-channel baseline.
- Query resolution without human escalation for a target % of informational (non-eligibility) questions.
- Equivalent-quality answers across Bangla dialectal variation and low-literacy phrasing, measured by a bias/quality audit (see `06-ai-risks.md`).
- No citizen data breach or unauthorised access incident.
