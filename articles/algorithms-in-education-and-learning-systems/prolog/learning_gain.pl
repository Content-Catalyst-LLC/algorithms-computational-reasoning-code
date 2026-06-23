learning_gain(Pretest, Posttest, Gain) :-
    Gain is Posttest - Pretest.

% Query example:
% ?- learning_gain(0.52, 0.78, Gain).
