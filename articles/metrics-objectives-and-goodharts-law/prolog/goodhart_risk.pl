risk_score(ProxyGap, Pressure, Gaming, GuardrailPenalty, Score) :-
    Score is (ProxyGap + Pressure + Gaming + GuardrailPenalty) / 4.

% Query example:
% ?- risk_score(0.38, 0.88, 0.72, 1.0, Score).
