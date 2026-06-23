unary_increment(Input, Output) :-
    append(Ones, ['_'|Rest], Input),
    all_ones(Ones),
    append(Ones, ['1','_'|Rest], Output).

all_ones([]).
all_ones(['1'|Rest]) :- all_ones(Rest).

% Query example:
% ?- unary_increment(['1','1','1','_'], Output).
