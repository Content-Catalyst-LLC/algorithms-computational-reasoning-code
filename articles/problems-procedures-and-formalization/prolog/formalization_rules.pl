case('Document search', 82, 78, 70, 58, 56).
case('Worker scheduling', 72, 76, 58, 54, 62).
case('Public service triage', 60, 72, 52, 46, 66).
case('Scientific simulation', 86, 80, 76, 84, 70).

formalization_score(Name, Score) :-
    case(Name, Input, Output, Objective, Assumptions, Governance),
    Score is 0.20*Input + 0.20*Output + 0.25*Objective + 0.20*Assumptions + 0.15*Governance.
