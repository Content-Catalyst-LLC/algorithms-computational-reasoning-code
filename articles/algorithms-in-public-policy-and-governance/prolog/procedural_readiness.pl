procedural_readiness(DueProcess, Transparency, HumanReview, AppealReadiness, Score) :-
    Score is (DueProcess + Transparency + HumanReview + AppealReadiness) / 4.

% Query example:
% ?- procedural_readiness(0.58, 0.52, 0.60, 0.54, Score).
