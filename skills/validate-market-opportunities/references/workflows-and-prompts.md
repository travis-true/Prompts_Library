# Workflows and reusable prompts

## On-demand product validation

1. State the proposed buyer, problem, outcome, format, price, and channel.
2. Find current paid alternatives and first-party buyer-intent signals.
3. Harvest at least five relevant complaints across at least two independent sources when available.
4. Identify the repeated failure and costly workaround.
5. Design the smallest complete gap closer.
6. Apply the buyer-intent gate and scoring model.
7. Recommend Build now, Validate first, Improve/relaunch, Monitor, Reject, or Passion project.

### Copy-ready prompt

> Validate this idea as a commercial offer: [idea]. Buyer: [buyer]. Channel: [channel]. Price hypothesis: [price]. Use live web research and any first-party analytics provided. Apply the buyer-intent gate, complaint harvester, market-gap analysis, smallest-complete gap closer, weighted score, safest validation test, and a build/no-build decision. Separate verified facts, estimates, and inferences and cite each current claim.

## Complaint harvester

Search dated reviews, buyer questions, forums, social posts, and first-party feedback. Prioritize complaints tied to money, time, risk, implementation failure, or unmet outcomes.

### Copy-ready prompt

> Find repeated complaints from [buyer] about [product/category] within the last [window]. Capture the buyer's context, complaint, workaround, consequence, date, URL, and whether the complaint repeats independently. Cluster complaints by job-to-be-done. Do not treat one anecdote as a trend. Identify which complaints signal willingness to pay and which are merely preferences.

## Market gap analysis

Compare top paid offers and complaint clusters. Distinguish missing content from implementation burden, weak proof, poor usability, lack of customization, maintenance cost, and channel mismatch.

### Copy-ready prompt

> Compare the strongest paid offers for [category]. For each, record buyer, price, format, promise, components, proof, implementation burden, and repeated complaints. Identify the most common high-consequence job that remains unsolved. State the gap in one sentence and label it as verified fact or inference.

## Gap closer

Create the smallest offer that produces the promised outcome without reproducing competitor bloat.

### Copy-ready prompt

> Design the smallest complete offer for this market gap: [gap]. Include buyer, transformation, must-have components, implementation path, proof mechanism, format, price range, licensing, differentiation, exclusions, creation estimate, and safest validation test. Every component must directly close a documented complaint.

## Store audit

Audit each funnel stage separately:

1. Exposure: impressions/page views and traffic sources
2. Click/interest: previews, saves, wishlists, and product-page engagement
3. Purchase intent: checkout starts, questions, sample downloads
4. Conversion: purchases divided by relevant traffic
5. Offer: outcome, audience, completeness, differentiation
6. Trust: previews, examples, reviews, credentials, policies
7. Findability: title, keywords, category, tags, first 160 characters
8. Pricing: comparable paid alternatives, perceived value, licensing

Do not call a product-market failure when exposure is too low to test conversion.

## Weekly scan

Cover the previous seven days and compare with the prior four weeks.

- Identify new buyer-intent signals, complaints, regulations, product launches, pricing changes, and marketplace movement.
- Update only opportunities whose evidence or score changed.
- Report new signals, score changes, emerging opportunities, weakening opportunities, and one recommended action.
- Use a durable scan date and cite every current claim.

### Copy-ready prompt

> Run the weekly market-intelligence scan for the defined niches. Cover the last seven days, compare with the prior four weeks, update buyer-intent evidence and scores, and report only material changes. Rank the three best actions for the next seven days. Use the system's source tiers, buyer-intent gate, and fact/estimate/inference labels.

## Monthly review

Cover the previous calendar month and refresh 30-day, 90-day, and 12-month context.

- Re-score every active opportunity.
- Review first-party traffic, checkout, and sales data.
- Promote, demote, reject, or archive opportunities.
- Compare completed experiments with their success thresholds.
- Select one monthly build/relaunch priority and one validation priority.

### Copy-ready prompt

> Run the monthly market review. Refresh 30-day momentum, 90-day validation, and 12-month context; re-score all active opportunities; audit current store performance; record completed experiments; and select one build/relaunch priority plus one validation priority. Explain every decision change and cite current evidence.
