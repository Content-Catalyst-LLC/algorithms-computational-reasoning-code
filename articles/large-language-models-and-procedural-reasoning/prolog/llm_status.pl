status(Score, high, escalate) :- Score < 1.0, !.
status(Score, _, pass) :- Score >= 0.8, !.
status(_, _, review).
