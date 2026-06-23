automation_risk(Stakes, Opacity, Delegation, Irreversibility, Risk) :-
    Raw is Stakes * Opacity * Delegation * Irreversibility,
    Risk is max(0.0, min(1.0, Raw)).

% Query example:
% ?- automation_risk(0.95, 0.85, 0.90, 0.80, Risk).
