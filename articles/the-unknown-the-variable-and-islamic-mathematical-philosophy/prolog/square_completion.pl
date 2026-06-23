square_completion(B, C, Completion, CompletedRhs) :-
    Completion is (B / 2) * (B / 2),
    CompletedRhs is C + Completion.

% Query example:
% ?- square_completion(10, 39, Completion, CompletedRhs).
