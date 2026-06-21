generalization_gap(Train, Test, Gap) :- Gap is Train - Test.
:- initialization(main).
main :- generalization_gap(0.88, 0.81, Gap), writeln(Gap), halt.
