query_logic_score(entity, relationship, predicate, join, keys, missingness) = 100 * (0.18*entity + 0.18*relationship + 0.18*predicate + 0.18*join + 0.14*keys + 0.14*missingness)
println("test_name,value")
println("query_logic_core_score,$(query_logic_score(.88,.86,.84,.82,.84,.80))")
