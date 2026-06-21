expected_net_value(P, Benefit, Loss, Cost, Value) :-
    Bounded is max(0, min(1, P)),
    Value is Bounded * Benefit - Bounded * Loss - Cost.

% Example:
% ?- expected_net_value(0.42, 150, 80, 25, V).
