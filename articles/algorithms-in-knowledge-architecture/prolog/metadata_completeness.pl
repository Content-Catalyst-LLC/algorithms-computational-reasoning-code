metadata_completeness(PresentFields, RequiredFields, Score) :-
    RequiredFields > 0,
    Score is PresentFields / RequiredFields.

% Query example:
% ?- metadata_completeness(11, 12, Score).
