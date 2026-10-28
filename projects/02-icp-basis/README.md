# 02 · ICP & account research: Basis

## Problem
Basis sells AI agents to accounting firms. A BDR selling it needs to know **which firms** to target, **when** to reach them, and **who** inside each firm to talk to. Accounting firms buy very differently from tech companies (partnerships, private-equity owners, busy seasons), so a generic SaaS playbook doesn't work.

## Approach
1. **ICP:** define the target firm, signals, personas, negative ICP, and a 100-point scoring rubric
2. **TAM:** build the account universe from public firm rankings (Accounting Today Top 100, IPA Top 400)
3. **Signals:** private-equity deals, mergers, hiring spikes, new CAS practices
4. **Account research:** full 5-part research (company, contacts, opportunity, competition, strategy) on the top-scoring firms
5. **Outreach angles:** messages built around each firm's own signal and the busy-season calendar

## Product
[Basis](https://www.getbasis.ai): AI agents for accounting, tax, and audit. $138M raised; $1.15B valuation (Feb 2026) *(reported)*.

## Output
- ✅ [Ideal customer profile](IDEAL-CUSTOMER-PROFILE.md), including a Clay vs. Basis comparison of how the ICP changes by market
- ✅ **Target account list:** [`build_target_list.py`](build_target_list.py) applies the ICP rules to the [IPA Top 500](https://insidepublicaccounting.com/ipa-top-500-firms/) ranking (top 150 firms, 2026) and writes [`data/target-accounts.csv`](data/target-accounts.csv)
  | Status | Firms | Meaning |
  |---|---|---|
  | tier 1 | 111 | In the sweet spot ($39M–$600M revenue) |
  | tier 2 | 16 | Very large firms: enterprise-style sale |
  | check | 4 | Specialist firms; a human reviews first |
  | remove | 19 | Big 4 (4) + existing Basis customers (15) |

  Run it: `python3 build_target_list.py` (standard library only)
- ⏳ Signal checks and scores for the top tier 1 firms
- ⏳ Prospect reports for the top 3 firms

## What I learned
Coming soon.

## Credits
Research method adapted from [AI Sales Team for Claude Code](https://github.com/zubair-trabzada/ai-sales-team-claude) (MIT).
