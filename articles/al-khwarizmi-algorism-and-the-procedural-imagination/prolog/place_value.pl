place_value(Digit, Base, Position, Value) :-
    Value is Digit * Base ** Position.

% Query example:
% ?- place_value(7, 10, 3, Value).
