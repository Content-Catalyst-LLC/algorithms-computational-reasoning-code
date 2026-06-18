using Random, Statistics
Random.seed!(20260617)
function monte_carlo_pi(trials)
    inside = 0
    for _ in 1:trials
        x = rand(); y = rand()
        inside += (x^2 + y^2 <= 1) ? 1 : 0
    end
    return 4 * inside / trials
end
println("test_name,value")
println("monte_carlo_pi,$(monte_carlo_pi(5000))")
println("amplification_failure,$(0.1^5)")
