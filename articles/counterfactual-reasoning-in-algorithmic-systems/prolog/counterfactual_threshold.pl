label(Score, Threshold, favorable) :- Score >= Threshold.
label(Score, Threshold, not_favorable) :- Score < Threshold.

flipped(Original, Counterfactual, Threshold) :-
    label(Original, Threshold, L1),
    label(Counterfactual, Threshold, L2),
    L1 \= L2.

:- initialization(main).
main :-
    (flipped(0.57, 0.65, 0.62) -> writeln(decision_flipped_true); writeln(decision_flipped_false)),
    halt.
