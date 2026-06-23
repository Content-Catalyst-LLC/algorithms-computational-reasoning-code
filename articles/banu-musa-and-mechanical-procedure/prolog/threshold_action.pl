action_triggered(Level, Threshold) :-
    Level >= Threshold.

% Query example:
% ?- action_triggered(7.5, 5.0).
