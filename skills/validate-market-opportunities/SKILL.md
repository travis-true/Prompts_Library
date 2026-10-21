---
name: validate-market-opportunities
description: "Research, validate, score, and monitor commercial product or service opportunities using live buyer-intent evidence, complaint harvesting, market-gap analysis, competitor review, store analytics, and smallest-complete-offer design. Use for market scans, trend reports, product validation, opportunity ranking, marketplace audits, product positioning, launch/no-launch decisions, or recurring weekly and monthly market intelligence."
---

# Validate market opportunities

Use current web research and the user's first-party analytics to identify offers likely to sell. Separate verified facts, estimates, and inferences. Never equate attention with purchase intent.

## Load the right context

- Read `references/business-context.md` and complete its workplace business-context fields before applying specific assumptions.
- Read `references/evidence-and-sources.md` before live research.
- Read `references/scoring-model.md` before scoring or ranking.
- Read `references/workflows-and-prompts.md` for complaint harvesting, gap analysis, gap closing, store audits, and recurring scans.
- Read `references/output-schema.md` before producing or updating a tracker.

## Run the workflow

1. Define the buyer, urgent job, offer format, channel, geography, and decision deadline. Ask one strategic question only if a missing answer would materially change the work.
2. Establish the first-party baseline: inventory, price, age, page views, previews, wish lists, checkout starts, sales, conversion, traffic source, reviews, and prior experiments.
3. Scan 30-day momentum, 90-day validation, and 12-month context. Use direct links and dates. Prefer first-party buyer behavior and primary sources.
4. Apply the buyer-intent gate. Require at least two independent signals, including one hard signal: transactions, paid listings with reviews, purchase requests, budgets, procurement activity, a binding deadline, or first-party conversion data.
5. Harvest repeated complaints in buyers' own language. Record source, date, audience, product/category, complaint, workaround, consequence, and frequency. Avoid isolated anecdotes.
6. Compare leading offers. Identify what buyers receive, price, format, proof, implementation burden, recurring complaints, and unresolved jobs.
7. State the market gap as: `[buyer] needs [outcome] without [repeated failure] because [consequence]. Existing offers fail by [pattern].`
8. Design the smallest complete gap closer. Include the core outcome, must-have components, proof mechanism, delivery format, price hypothesis, channel, differentiator, and explicit exclusions.
9. Score every candidate with `references/scoring-model.md`. Run `scripts/score_opportunities.py` for CSV inputs when useful.
10. Assign a decision: Build now, validate first, improve/relaunch, monitor, reject, or passion-project backlog. Explain the evidence threshold behind the decision.
11. For existing products, diagnose exposure, click-through, conversion, offer, trust, preview, SEO, pricing, and channel fit separately. Do not infer product-market failure from low traffic alone.
12. Preserve an evidence trail: exact URLs, publication dates, accessed date, claim supported, evidence tier, confidence, and whether the item is fact, estimate, or inference.

## Apply operating rules

- Favor the smallest complete offer; never add pages or features as filler.
- Prefer downloadable resources, AI workflow systems, short courses, licensing bundles, productized services, live training, then memberships unless evidence favors another format.
- Reject commercial ideas that fail the buyer-intent gate. Keep meaningful unsupported ideas in a clearly labeled passion-project backlog.
- Treat competitor counts, search results, social engagement, and trend articles as supporting evidence—not proof of demand.
- Distinguish discoverability failure from conversion failure and product-market failure.
- Use only independently created, public-domain, or properly licensed material. Never use employer files, wording, examples, branding, confidential information, or proprietary processes.
- Recheck unstable claims live. Cite sources near each claim.
- Recommend a safe validation method that does not require preorders unless the user requests them.

## Finish with action

Lead with the decision. Include the top opportunity, why now, buyer, gap closer, score, confidence, safest validation test, next action, and what evidence would reverse the decision. For scans, rank three opportunities per requested niche and identify the overall top three.
