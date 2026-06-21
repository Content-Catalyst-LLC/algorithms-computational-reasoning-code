proxy_risk(application_completeness, high).
proxy_risk(prior_access, high).
needs_review(Feature) :- proxy_risk(Feature, high).
