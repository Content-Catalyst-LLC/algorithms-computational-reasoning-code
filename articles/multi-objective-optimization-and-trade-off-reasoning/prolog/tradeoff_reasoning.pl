% Simple trade-off facts.
alternative(a, 72, 34, 82).
alternative(b, 64, 41, 76).
alternative(c, 81, 26, 88).
alternative(d, 58, 52, 69).

acceptable(Name) :- alternative(Name, Cost, Risk, Quality), Cost =< 85, Risk =< 40, Quality >= 75.
