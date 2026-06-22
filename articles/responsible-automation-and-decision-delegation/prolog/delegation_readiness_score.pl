delegation_readiness_score(Evidence, Validation, Reversibility, Contestability, Governance, HumanReview, Score) :-
    Score is (Evidence + Validation + Reversibility + Contestability + Governance + HumanReview) / 6.

% Query example:
% ?- delegation_readiness_score(0.62, 0.58, 0.46, 0.52, 0.60, 0.58, Score).
