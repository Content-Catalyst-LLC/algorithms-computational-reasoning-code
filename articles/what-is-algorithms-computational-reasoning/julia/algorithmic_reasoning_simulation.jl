println("scenario,input_size,estimated_n_log_n,estimated_quadratic,warning")
for scenario in ["Brute-force procedure", "Indexed search design", "Graph-aware reasoning", "Governed computational reasoning"]
    for power in 4:14
        n = 2^power
        println(join((scenario, n, round(n * log2(n), digits=3), n*n, "Synthetic complexity comparison only."), ","))
    end
end
