historical_risk_score(ProvenanceRisk, MeasurementWeakness, ProxyRisk, Remediation, Score) :-
    Score is (ProvenanceRisk + MeasurementWeakness + ProxyRisk + (1 - Remediation)) / 4.

% Query example:
% ?- historical_risk_score(0.66, 0.58, 0.62, 0.42, Score).
