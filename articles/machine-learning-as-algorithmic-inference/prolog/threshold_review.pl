rate(TP, FP, TN, FN, Accuracy, Precision, Recall) :-
    Total is TP + FP + TN + FN,
    Accuracy is (TP + TN) / Total,
    Precision is TP / (TP + FP),
    Recall is TP / (TP + FN).

:- initialization(main).
main :-
    rate(80, 25, 140, 35, Accuracy, Precision, Recall),
    format('accuracy=~6f~n', [Accuracy]),
    format('precision=~6f~n', [Precision]),
    format('recall=~6f~n', [Recall]),
    halt.
