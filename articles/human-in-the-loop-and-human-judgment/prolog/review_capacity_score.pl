review_capacity_score(Time, Information, Authority, Training, Protection, Score) :-
    Score is (Time + Information + Authority + Training + Protection) / 5.

% Query example:
% ?- review_capacity_score(0.56, 0.62, 0.58, 0.60, 0.48, Score).
