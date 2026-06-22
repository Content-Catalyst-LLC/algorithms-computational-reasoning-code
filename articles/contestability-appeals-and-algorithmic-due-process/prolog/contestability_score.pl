contestability_score(Notice, Reasons, EvidenceAccess, HumanReview, Correction, Remedy, Score) :-
    Score is (Notice + Reasons + EvidenceAccess + HumanReview + Correction + Remedy) / 6.

% Query example:
% ?- contestability_score(0.70, 0.62, 0.48, 0.55, 0.52, 0.44, Score).
