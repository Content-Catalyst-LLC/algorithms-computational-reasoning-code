score(TextMatch, Quality, Freshness, DiversityBonus, RiskPenalty, Score) :-
    Score is 0.36*TextMatch + 0.30*Quality + 0.16*Freshness + 0.14*DiversityBonus - 0.20*RiskPenalty.
eligible(a). eligible(b). eligible(d). eligible(e).
