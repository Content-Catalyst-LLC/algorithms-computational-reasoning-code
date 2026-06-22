governance_readiness_score(Ownership, Documentation, Monitoring, Contestability, Remediation, StopAuthority, Score) :-
    Score is (Ownership + Documentation + Monitoring + Contestability + Remediation + StopAuthority) / 6.

% Query example:
% ?- governance_readiness_score(0.60, 0.62, 0.58, 0.52, 0.46, 0.50, Score).
