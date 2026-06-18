precision(tp, retrieved) = retrieved == 0 ? 0 : tp / retrieved
recall(tp, relevant) = relevant == 0 ? 0 : tp / relevant
println("test_name,value")
println("precision,$(precision(2,3))")
println("recall,$(recall(2,2))")
