harm_risk_score(ErrorLikelihood, Severity, Exposure, Contestability, HarmRisk) :-
    HarmRisk is ErrorLikelihood * Severity * Exposure * (1 - Contestability).

% Query example:
% ?- harm_risk_score(0.34, 0.92, 0.78, 0.42, HarmRisk).
