readiness(Threat, Surface, Monitoring, Defense, Incident, Governance, Score) :-
    Score is 100 * (0.18*Threat + 0.18*Surface + 0.18*Monitoring + 0.18*Defense + 0.14*Incident + 0.14*Governance).

:- initialization(main).
main :-
    readiness(0.86, 0.82, 0.88, 0.82, 0.80, 0.78, Score),
    format('adversarial readiness=~3f~n', [Score]),
    halt.
