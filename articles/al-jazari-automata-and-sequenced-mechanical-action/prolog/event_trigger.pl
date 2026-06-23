event_triggered(Value, Trigger) :-
    Value >= Trigger.

% Query example:
% ?- event_triggered(12.0, 10.0).
