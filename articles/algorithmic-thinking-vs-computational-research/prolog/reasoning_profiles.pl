profile('Recipe-like procedure', 86, 72, 70, 62, 42, 20).
profile('Classroom algorithm exercise', 90, 82, 84, 78, 62, 32).
profile('Search and ranking system', 72, 70, 76, 66, 78, 70).
profile('Public decision-support workflow', 68, 66, 64, 72, 80, 86).
profile('Scientific modeling workflow', 74, 78, 76, 82, 86, 74).

algorithmic_score(Name, Score) :-
    profile(Name, Step, Decomp, Control, Test, _, _),
    Score is 0.28*Step + 0.24*Decomp + 0.24*Control + 0.24*Test.

computational_score(Name, Score) :-
    profile(Name, Step, Decomp, Control, Test, Representation, Governance),
    Score is 0.16*Step + 0.14*Decomp + 0.14*Control + 0.14*Test + 0.22*Representation + 0.20*Governance.
