# Output and tracker schema

## Opportunity record

Use one row per opportunity with these fields:

opportunity_id, scan_date, niche, buyer, urgent_job, offer_name, offer_format, channel, geography, momentum_30d, validation_90d, context_12m, hard_intent_signal, complaint_pattern, market_gap, gap_closer, price_hypothesis, validation_test, demand, urgency, willingness_to_pay, competition_advantage, differentiation, speed_to_create, audience_access, channel_fit, expertise_alignment, weighted_score, confidence, decision, next_action, reversal_evidence, source_urls

## Evidence record

Use one row per claim:

evidence_id, opportunity_id, accessed_date, published_date, source_title, url, source_type, evidence_tier, buyer_role, claim_supported, complaint_or_signal, fact_estimate_inference, confidence, notes

## Store-audit record

Use one row per product:

product_id, channel, title, url, posted_date, price, audience, format, page_views, previews, wishlists, checkout_starts, sales, conversion_rate, reviews, traffic_source, exposure_diagnosis, click_diagnosis, conversion_diagnosis, offer_diagnosis, seo_diagnosis, preview_diagnosis, pricing_diagnosis, trust_diagnosis, decision, priority_action

## Required report order

1. Decision summary
2. Baseline and funnel diagnosis
3. Overall top three opportunities
4. Three opportunities per niche
5. Complaint-harvester findings
6. Market gaps and gap closers
7. Existing-store audit
8. Rejected ideas and passion-project backlog
9. 30/60/90-day action plan
10. Evidence register and limitations

Keep facts, estimates, and inferences visibly labeled.
