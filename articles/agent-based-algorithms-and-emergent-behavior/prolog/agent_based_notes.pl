review_layer(agents).
review_layer(rules).
review_layer(environment).
review_layer(interaction).
review_layer(emergence).
review_layer(governance).

requires_review(emergent_claim) :- review_layer(rules), review_layer(validation).
