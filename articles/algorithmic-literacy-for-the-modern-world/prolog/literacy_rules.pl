case('Search ranking', 62, 66, 38, 52, 68).
case('Public decision-support workflow', 58, 56, 70, 76, 74).
case('Scientific simulation dashboard', 76, 74, 60, 68, 80).
case('Recommendation feed', 40, 48, 32, 46, 50).

literacy_support_score(Name, Score) :-
    case(Name, Transparency, Interpretability, Contestability, Governance, Judgment),
    Score is 0.22*Transparency + 0.22*Interpretability + 0.18*Contestability + 0.18*Governance + 0.20*Judgment.
