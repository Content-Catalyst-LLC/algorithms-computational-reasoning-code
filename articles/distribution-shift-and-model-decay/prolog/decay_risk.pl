decay_risk(InputDrift, LabelDrift, PerformanceDecay, CalibrationGap, SubgroupGap, OverrideRate, Score) :-
    Score is (InputDrift + LabelDrift + PerformanceDecay + CalibrationGap + SubgroupGap + OverrideRate) / 6.

% Query example:
% ?- decay_risk(0.31, 0.16, 0.10, 0.14, 0.15, 0.11, Score).
