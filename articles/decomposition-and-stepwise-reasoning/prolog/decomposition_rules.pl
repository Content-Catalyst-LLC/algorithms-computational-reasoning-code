case('Search system', 82, 78, 82, 72, 72).
case('Public decision-support workflow', 74, 66, 68, 60, 58).
case('Scientific simulation', 86, 82, 80, 78, 82).
case('Knowledge architecture', 80, 76, 74, 70, 80).

decomposition_score(Name, Score) :-
    case(Name, Subproblem, Boundary, Sequencing, Dependencies, Recomposition),
    Score is 0.22*Subproblem + 0.20*Boundary + 0.18*Sequencing + 0.20*Dependencies + 0.20*Recomposition.
