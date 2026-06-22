selection_gap(A, B, C, Gap) :-
    Max is max(A, max(B, C)),
    Min is min(A, min(B, C)),
    Gap is Max - Min.

% Query example:
% ?- selection_gap(0.42, 0.31, 0.36, Gap).
