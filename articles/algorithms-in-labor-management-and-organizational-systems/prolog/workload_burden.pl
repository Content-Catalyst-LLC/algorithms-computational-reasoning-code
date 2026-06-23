workload_burden(Pace, Hours, Fatigue, ScheduleVolatility, Burden) :-
    Burden is (Pace + Hours + Fatigue + ScheduleVolatility) / 4.

% Query example:
% ?- workload_burden(0.84, 0.72, 0.70, 0.78, Burden).
