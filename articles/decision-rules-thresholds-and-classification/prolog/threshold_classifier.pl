classify(Score, Threshold, 1) :- Score >= Threshold, !.
classify(_, _, 0).

:- initialization(main).
main :-
    classify(0.72, 0.50, Label),
    writeln(Label),
    halt.
