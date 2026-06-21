generalization_gap(Train, Test, Gap) :- Gap is Test - Train.
:- initialization(main).
main :- generalization_gap(0.04, 0.09, Gap), writeln(Gap), halt.
