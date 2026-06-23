sensitivity(TP, FN, Sensitivity) :-
    Sensitivity is TP / (TP + FN).

% Query example:
% ?- sensitivity(86, 14, Sensitivity).
