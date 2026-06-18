precision_at_k(tp, k) = k == 0 ? 0 : tp / k
weighted_score(lexical, metadata, freshness, authority, semantic, provenance) = 100 * (0.22*lexical + 0.18*metadata + 0.12*freshness + 0.16*authority + 0.17*semantic + 0.15*provenance)
println("test_name,value")
println("precision_at_3,$(precision_at_k(2,3))")
println("ranking_signal_score,$(weighted_score(.84,.88,.76,.82,.78,.86))")
