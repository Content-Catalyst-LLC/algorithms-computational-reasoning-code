function dijkstra_small()
    # Teaching-only compact example for a fixed graph.
    dist = Dict("A" => 0.0, "B" => 3.0, "C" => 2.0, "D" => 8.0, "E" => 10.0)
    for key in sort(collect(keys(dist)))
        println(key, "=", dist[key])
    end
end

dijkstra_small()
