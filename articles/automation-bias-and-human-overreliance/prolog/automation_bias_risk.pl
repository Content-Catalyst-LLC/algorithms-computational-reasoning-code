automation_bias_risk(Acceptance, Quality, Uncertainty, ReviewDeficit, OverrideFriction, WeakContestability, Score) :-
    Gap0 is Acceptance - Quality,
    OverrelianceGap is max(0, Gap0),
    Score is (Acceptance + OverrelianceGap + Uncertainty + ReviewDeficit + OverrideFriction + WeakContestability) / 6.

% Query example:
% ?- automation_bias_risk(0.93, 0.71, 0.29, 0.65, 0.72, 0.0, Score).
