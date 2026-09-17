# 2. Stakeholder Map

Each stakeholder group is listed with their **stake**, **power to influence the system**, and **risk if ignored**.

## Government (ICT Division / a2i, relevant line ministries, 333 Helpline)
- **Stake**: Digital Bangladesh / Smart Bangladesh policy delivery, cost reduction on the 333 helpline, political accountability if the bot gives wrong information.
- **Power**: High — funds and can mandate/cancel the project, owns underlying data and legal authority.
- **Risk if ignored**: Misalignment with existing e-Government Interoperability Framework; duplicated effort with other ongoing a2i initiatives.

## Citizens (general public, primary users)
- **Stake**: Faster, clearer access to services; risk of acting on wrong AI guidance.
- **Power**: Low individually, but collective trust/adoption determines whether the system succeeds — low trust means citizens simply go back to informal intermediaries.
- **Risk if ignored**: The system becomes a compliance exercise that nobody actually uses, or worse, actively misleads people who have no easy way to challenge a wrong answer.

## Developers / implementation team
- **Stake**: Building something technically sound, defensible, and maintainable; professional/reputational stake in the system not causing a public incident.
- **Power**: Medium-high in the design phase (architecture, model choice, guardrails); low once deployed and governance shifts to operations.
- **Risk if ignored**: Governance requirements bolted on after launch are far more expensive and often technically incompatible with early architecture decisions.

## Data administrators (data owners, IT/security teams within the relevant ministries)
- **Stake**: Being accountable for data they didn't necessarily choose to expose to a new AI system; audit and compliance burden.
- **Power**: High — can block data access, set retention/access-control policy.
- **Risk if ignored**: Shadow data flows, unclear ownership when something goes wrong, resistance that stalls the project indefinitely.

## Vulnerable groups (rural, low-literacy, elderly, persons with disabilities, linguistic minorities, women with limited independent phone/internet access)
- **Stake**: This group has the most to gain from equitable access *and* the most to lose from a system that performs worse for them (e.g. bot trained mostly on standard Dhaka-dialect, formal-register Bangla).
- **Power**: Very low — rarely consulted directly in system design.
- **Risk if ignored**: The system widens rather than closes the access gap it was built to close; this is the single biggest reputational and ethical risk in the whole project, and is the reason `06-ai-risks.md` treats bias/discrimination as a first-class risk, not an afterthought.

## Secondary stakeholders (worth naming, easy to forget)
- **Civil society / RTI (Right to Information) advocates**: will scrutinise data practices and transparency.
- **Journalists/media**: first place a governance failure becomes a public story.
- **Academic/research community**: potential source of bias-audit expertise and external validation.
- **Telecom/SMS gateway providers**: operational dependency for the low-bandwidth channel, with their own data-handling practices to account for.

## Stakeholder conflict points to design around
- **Government (speed/cost savings) vs. Data administrators (caution/compliance)**: resolved via the phased scope in `01` — no live database integration until governance is proven.
- **Developers (model capability) vs. Vulnerable groups (equity)**: resolved by making dialect/literacy performance an explicit, measured requirement, not a "nice to have."
