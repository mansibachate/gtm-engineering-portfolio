# GTM Engineering Portfolio

Systems that help B2B teams find the right accounts at the right time and reach them with relevant messages.

This repo collects the go-to-market workflows I build: account research, lead qualification, enrichment, signal-based prospecting, and outreach. Each project has a short write-up covering the problem, how the system works, and what came out of it.

## Focus areas

- **Account research & qualification:** turning a company URL into a scored fit assessment (firmographics, BANT/MEDDIC, buying committee)
- **Signal-based prospecting:** finding companies at the right moment (funding, hiring, leadership changes)
- **Enrichment:** waterfall data sourcing and validation
- **AI personalization:** outreach that references something real, not generic flattery
- **CRM & routing:** getting the right lead to the right rep, fast

## Projects

| # | Project | What it does | Status |
|---|---|---|---|
| 01 | [ICP & account research](projects/01-icp-account-research/) | Defines an ideal customer profile for a real SaaS product and runs AI-assisted research and scoring on target accounts | In progress |
| 02 | [ICP & account research: Basis](projects/02-icp-basis/) | The same method applied to a very different market: AI agents sold to accounting firms | In progress |
| 03 | Signal-based lead list | Finds companies showing a buying signal, identifies decision-makers, and drafts a personalized opener | Planned |
| 04 | Inbound lead router | Form → enrichment → scoring → CRM → Slack alert, built on open-source tools | Planned |

## Stack

Claude Code · Python · Clay · HubSpot · n8n · LLM APIs

## How each project is documented

Every project folder has a `README.md` with:

1. **Problem:** what a sales or marketing team is trying to do
2. **Approach:** the workflow, step by step
3. **Output:** sample results (real company data is from public sources only)
4. **What I learned:** what worked, what didn't, what I'd change

## Credits

Some projects build on open-source work, which is credited in each project's README:

- [AI Sales Team for Claude Code](https://github.com/zubair-trabzada/ai-sales-team-claude) (MIT)

## Contact

Open to GTM engineering, growth ops, and outbound roles, and to freelance projects. Reach out via [GitHub](https://github.com/mansibachate).
