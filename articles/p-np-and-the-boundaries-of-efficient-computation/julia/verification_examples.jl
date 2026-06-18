function verify_coloring(edges, coloring)
    all(coloring[u] != coloring[v] for (u,v) in edges)
end
println("test_name,value")
println("coloring_valid,$(verify_coloring([(1,2),(2,3)], Dict(1=>1,2=>2,3=>1)))")
