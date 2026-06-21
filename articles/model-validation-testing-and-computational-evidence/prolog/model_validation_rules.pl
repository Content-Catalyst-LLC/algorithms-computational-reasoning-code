% Simple validation evidence rules.
metric(candidate_model, rmse, 8.72).
metric(simple_baseline, rmse, 18.41).
check(intended_use_defined, pass).
check(data_quality_checked, pass).
check(sensitivity_reviewed, partial).

beats_baseline(Model) :-
  metric(Model, rmse, M),
  metric(simple_baseline, rmse, B),
  M < B.

needs_review(Check) :- check(Check, partial).
