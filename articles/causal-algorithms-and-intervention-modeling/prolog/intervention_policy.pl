% Compact Prolog example: intervention decision threshold.
decision(Score, Threshold, act) :- Score >= Threshold.
decision(Score, Threshold, monitor) :- Score < Threshold.
effect(Baseline, Intervention, Effect) :- Effect is Intervention - Baseline.

% Example queries:
% ?- effect(0.42, 0.57, E).
% ?- decision(0.53, 0.55, D).
