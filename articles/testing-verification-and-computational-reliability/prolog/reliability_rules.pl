score_in_range(X) :- X >= 0, X =< 100.
test_result(score_72, pass) :- score_in_range(72).
test_result(score_150, fail) :- \+ score_in_range(150).
reliability_property(score_range_invariant).
reliability_property(idempotency).
reliability_property(nondecreasing_order).
