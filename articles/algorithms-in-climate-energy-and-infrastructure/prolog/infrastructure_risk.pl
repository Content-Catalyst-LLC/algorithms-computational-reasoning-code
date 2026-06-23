infrastructure_risk(Hazard, Exposure, Vulnerability, Risk) :-
    Risk is Hazard * Exposure * Vulnerability.

% Query example:
% ?- infrastructure_risk(0.80, 0.75, 0.60, Risk).
