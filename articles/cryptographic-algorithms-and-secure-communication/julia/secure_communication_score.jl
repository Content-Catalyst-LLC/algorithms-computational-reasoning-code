score(threat_model, keys, validation, integrity, authentication) = 100.0 * (0.22 * threat_model + 0.24 * keys + 0.18 * validation + 0.18 * integrity + 0.18 * authentication)
println("standard secure channel score=", round(score(0.86, 0.82, 0.90, 0.86, 0.84), digits=2))
println("legacy manual transfer score=", round(score(0.36, 0.24, 0.18, 0.34, 0.28), digits=2))
