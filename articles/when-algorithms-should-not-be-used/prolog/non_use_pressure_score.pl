non_use_pressure_score(Stakes, Irreversibility, GovernanceWeakness, ProxyIllegitimacy, Score) :-
    Score is (Stakes + Irreversibility + GovernanceWeakness + ProxyIllegitimacy) / 4.

% Query example:
% ?- non_use_pressure_score(0.94, 0.78, 0.56, 0.70, Score).
