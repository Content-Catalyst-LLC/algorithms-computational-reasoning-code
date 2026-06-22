current_stock = 100.0
inflow = 12.0
outflow = 7.0
next_stock = current_stock + inflow - outflow
println("next_stock=", round(next_stock, digits=4))
