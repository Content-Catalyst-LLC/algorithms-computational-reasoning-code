feedback_risk(Amplification, Concentration, Intervention, Drift, RecursiveData, Score) :-
    Score is (Amplification + Concentration + Intervention + Drift + RecursiveData) / 5.

% Query example:
% ?- feedback_risk(0.82, 0.76, 0.44, 0.28, 0.31, Score).
