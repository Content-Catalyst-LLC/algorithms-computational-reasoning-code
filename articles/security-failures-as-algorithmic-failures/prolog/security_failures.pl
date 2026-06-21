weight(0.08). weight(0.10). weight(0.10). weight(0.10). weight(0.08). weight(0.08). weight(0.08).
weight(0.08). weight(0.08). weight(0.08). weight(0.06). weight(0.05). weight(0.03).
score(S) :- findall(W, weight(W), Ws), sum_list(Ws, Total), S is 0.65 * Total * 100.
:- initialization((score(S), write(S), nl, halt)).
