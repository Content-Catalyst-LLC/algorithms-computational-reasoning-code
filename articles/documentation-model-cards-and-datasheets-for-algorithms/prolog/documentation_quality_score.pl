documentation_quality_score(Accuracy, Completeness, Specificity, Timeliness, Accessibility, Actionability, Score) :-
    Score is (Accuracy + Completeness + Specificity + Timeliness + Accessibility + Actionability) / 6.

% Query example:
% ?- documentation_quality_score(0.62, 0.6875, 0.58, 0.50, 0.56, 0.52, Score).
