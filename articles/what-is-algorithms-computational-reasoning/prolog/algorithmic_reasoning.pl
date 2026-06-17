scenario('Brute-force procedure', 40, 28, 20, 92).
scenario('Indexed search design', 62, 52, 38, 42).
scenario('Graph-aware reasoning', 76, 68, 54, 30).
scenario('Governed computational reasoning', 86, 82, 86, 18).

score(Name, Score) :-
    scenario(Name, Representation, Correctness, Governance, BruteForce),
    Raw is 0.30 * Representation + 0.30 * Correctness + 0.30 * Governance - 0.10 * BruteForce,
    Score is max(0, min(100, Raw)).
