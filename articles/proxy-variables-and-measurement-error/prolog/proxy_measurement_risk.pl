measurement_risk(ValidityGap, Missingness, DifferentialError, LabelError, Score) :-
    Score is (ValidityGap + Missingness + DifferentialError + LabelError) / 4.

% Query example:
% ?- measurement_risk(0.42, 0.12, 0.24, 0.08, Score).
