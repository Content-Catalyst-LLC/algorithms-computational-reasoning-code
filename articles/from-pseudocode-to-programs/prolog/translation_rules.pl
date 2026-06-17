case('Search ranking prototype', 82, 80, 64, 68, 72).
case('Decision-rule implementation', 76, 74, 66, 62, 68).
case('Simulation loop', 84, 82, 72, 70, 74).
case('Data-cleaning procedure', 78, 76, 70, 66, 72).

translation_quality(Name, Score) :-
    case(Name, Intent, Control, Edge, Tests, Maintain),
    Score is 0.22*Intent + 0.22*Control + 0.18*Edge + 0.18*Tests + 0.20*Maintain.
