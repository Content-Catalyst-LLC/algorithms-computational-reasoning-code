gcd_algorithm(A, 0, G) :- G is abs(A).
gcd_algorithm(A, B, G) :-
    B =\= 0,
    R is A mod B,
    gcd_algorithm(B, R, G).

% Query example:
% ?- gcd_algorithm(252, 105, G).
