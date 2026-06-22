explanation_quality_score(Faithfulness, Stability, Understandability, Actionability, Uncertainty, Score) :-
    Score is (Faithfulness + Stability + Understandability + Actionability + Uncertainty) / 5.

% Query example:
% ?- explanation_quality_score(0.70, 0.74, 0.62, 0.58, 0.46, Score).
