expected_loss(PD, LGD, EAD, ExpectedLoss) :-
    ExpectedLoss is PD * LGD * EAD.

% Query example:
% ?- expected_loss(0.035, 0.45, 100000, ExpectedLoss).
