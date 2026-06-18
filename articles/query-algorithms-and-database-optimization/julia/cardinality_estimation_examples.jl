selection_rows(table_rows, selectivity) = table_rows * selectivity
join_rows(left_rows, right_rows, left_distinct, right_distinct) = (left_rows * right_rows) / max(left_distinct, right_distinct)
println("test_name,value")
println("selection_estimated_rows,$(selection_rows(1000000,0.012))")
println("join_estimated_rows,$(join_rows(500000,200000,50000,40000))")
