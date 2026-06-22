failure_risk_score(Likelihood, Severity, Detectability, Controllability, FailureRisk) :-
    FailureRisk is Likelihood * Severity * (1 - Detectability) * (1 - Controllability).

% Query example:
% ?- failure_risk_score(0.42, 0.86, 0.38, 0.44, FailureRisk).
