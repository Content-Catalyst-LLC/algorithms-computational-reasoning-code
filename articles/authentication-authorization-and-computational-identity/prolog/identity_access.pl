weight(0.10). weight(0.11). weight(0.11). weight(0.09). weight(0.09). weight(0.10).
weight(0.09). weight(0.09). weight(0.08). weight(0.06). weight(0.06). weight(0.02).
score(S) :- findall(W, weight(W), Ws), sum_list(Ws, Total), S is 0.75 * Total * 100.
:- initialization((score(S), write(S), nl, halt)).
