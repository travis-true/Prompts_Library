# Opportunity scoring model

Score each factor from 0 to 5, then calculate the weighted score out of 100.

| Factor | Weight | 0 | 3 | 5 |
|---|---:|---|---|---|
| Demand | 15 | No buyer signal | Repeated interest plus some buying | Strong transactions, reviews, budgets, or procurement |
| Urgency | 15 | Optional someday | Active recurring pain | Deadline, compliance, acute cost, or immediate seasonal need |
| Willingness to pay | 10 | Free expectation | Comparable paid offers | Clear budgets or strong paid precedent |
| Competition advantage | 10 | Saturated and interchangeable | Crowded but gap exists | Weak alternatives or defensible white space |
| Differentiation | 10 | Commodity | Some meaningful distinction | Clear outcome/mechanism buyers can explain |
| Speed to create | 10 | More than 8 weeks | 2–4 weeks | 1 week or less using existing assets |
| Audience access | 10 | No reachable buyers | Reachable via one weak channel | Existing audience, search channel, or warm network |
| Channel fit | 10 | Poor purchasing fit | Viable with adaptation | Native fit for marketplace or direct sales |
| Expertise alignment | 10 | Outside credible scope | Adjacent capability | Strong proof and deep experience |

Formula: weighted score = sum(rating / 5 × weight)

## Decision thresholds

- 80–100: Build now, if the buyer-intent gate passes.
- 70–79: Validate first or improve/relaunch; build only when the hard signal is strong.
- 60–69: Monitor or run a small smoke test.
- Below 60: Reject for commercial priority.

## Confidence

- High: multiple Tier A sources and consistent first-party evidence.
- Medium: one Tier A source plus several Tier B sources.
- Low: incomplete first-party data, proxy-heavy evidence, or unresolved contradiction.

## Tie-breakers

1. Shorter time to a credible sale
2. Stronger owned or marketplace channel access
3. Greater reuse of existing high-quality assets
4. Higher price without adding delivery burden
5. Lower support and maintenance cost

Do not let a high score override a failed buyer-intent gate.
