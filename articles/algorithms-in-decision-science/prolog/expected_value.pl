expected_value(Probability, BenefitIfAct, CostIfAct, EV) :-
    EV is Probability * BenefitIfAct - CostIfAct.

% Query example:
% ?- expected_value(0.82, 0.88, 0.30, EV).
