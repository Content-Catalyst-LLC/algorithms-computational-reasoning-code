place_value(Digits, Value) :-
    place_value_acc(Digits, 0, Value).

place_value_acc([], Acc, Acc).
place_value_acc([D|Rest], Acc, Value) :-
    Next is Acc * 10 + D,
    place_value_acc(Rest, Next, Value).

% Query example:
% ?- place_value([1,2,3,0], Value).
