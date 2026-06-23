attention_risk(EngagementPressure, CreatorImpact, PublicKnowledgeImpact, UserControl, Contestability, Score) :-
    Score is (EngagementPressure + CreatorImpact + PublicKnowledgeImpact + (1 - UserControl) + (1 - Contestability)) / 5.

% Query example:
% ?- attention_risk(0.92, 0.88, 0.78, 0.44, 0.42, Score).
