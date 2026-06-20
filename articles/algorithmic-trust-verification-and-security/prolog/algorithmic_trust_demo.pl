trust_quality(Verification, Validation, Security, Provenance, Monitoring, Governance, Score) :-
    Score is 100 * (0.18*Verification + 0.18*Validation + 0.18*Security + 0.16*Provenance + 0.15*Monitoring + 0.15*Governance).

:- initialization(main).
main :-
    trust_quality(0.88, 0.82, 0.88, 0.90, 0.84, 0.82, Score),
    format('trust quality=~3f~n', [Score]),
    halt.
