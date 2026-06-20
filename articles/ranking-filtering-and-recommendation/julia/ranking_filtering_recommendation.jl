# Synthetic ranking score example in Julia.
function ranking_score(text_match, quality, freshness, diversity_bonus, risk_penalty)
    0.36 * text_match + 0.30 * quality + 0.16 * freshness + 0.14 * diversity_bonus - 0.20 * risk_penalty
end
println(round(ranking_score(0.92, 0.88, 0.60, 0.35, 0.04), digits=6))
