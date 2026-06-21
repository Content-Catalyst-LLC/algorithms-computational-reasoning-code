review_item(input_representation).
review_item(label_validity).
review_item(generalization).
review_item(interpretability).
review_item(use_boundary).

needs_review(input_representation).
needs_review(label_validity).
needs_review(interpretability).
needs_review(use_boundary).

requires_attention(Item) :- review_item(Item), needs_review(Item).
