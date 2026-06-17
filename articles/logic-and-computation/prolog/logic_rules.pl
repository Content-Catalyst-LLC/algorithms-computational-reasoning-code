case('Input validation rules', 82, 84, 68, 82, 70).
case('Database query constraints', 78, 80, 72, 76, 72).
case('Decision-rule workflow', 74, 70, 68, 72, 78).
case('Program invariant checks', 80, 78, 74, 80, 66).

logic_quality(Name, Score) :-
    case(Name, Rule, Predicate, Trace, Test, Governance),
    Score is 0.24*Rule + 0.24*Predicate + 0.20*Trace + 0.18*Test + 0.14*Governance.
