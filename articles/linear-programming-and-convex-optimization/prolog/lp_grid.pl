objective(X, Y, Value) :- Value is 3*X + 4*Y.
feasible(X, Y) :- X >= 0, Y >= 0, 2*X + Y =< 8, X + 2*Y =< 8.
solution(X, Y, Value) :- between(0, 9, X), between(0, 9, Y), feasible(X, Y), objective(X, Y, Value).
run :- findall(Value-X-Y, solution(X,Y,Value), Solutions), max_member(Best, Solutions), writeln(Best).
:- initialization(run, main).
