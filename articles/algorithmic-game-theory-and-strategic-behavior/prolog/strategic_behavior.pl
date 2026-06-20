payoff(cooperate, cooperate, 3, 3).
payoff(cooperate, defect, 0, 5).
payoff(defect, cooperate, 5, 0).
payoff(defect, defect, 1, 1).
welfare(P1, P2, W) :- payoff(P1, P2, U1, U2), W is U1 + U2.
