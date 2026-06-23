delegation_risk(DecisionSeverity, AutomationLevel, Opacity, Risk) :-
    Raw is DecisionSeverity * AutomationLevel * Opacity,
    Risk is max(0.0, min(1.0, Raw)).
