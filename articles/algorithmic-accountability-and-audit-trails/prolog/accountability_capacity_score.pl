accountability_capacity_score(Documentation, Provenance, Reviewability, Contestability, Remediation, Governance, Score) :-
    Score is (Documentation + Provenance + Reviewability + Contestability + Remediation + Governance) / 6.

% Query example:
% ?- accountability_capacity_score(0.72, 0.68, 0.64, 0.58, 0.52, 0.66, Score).
