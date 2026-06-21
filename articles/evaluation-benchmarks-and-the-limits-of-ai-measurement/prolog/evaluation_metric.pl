accuracy(TP, TN, FP, FN, Accuracy) :-
    Accuracy is (TP + TN) / (TP + TN + FP + FN).

% Query example:
% ?- accuracy(42, 38, 7, 13, A).
