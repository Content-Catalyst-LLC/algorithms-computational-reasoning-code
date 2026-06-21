# Minimal Julia validation metrics demo.
observed = [33.1, 39.7, 38.8, 39.3, 8.4]
predicted = [31.92, 31.58, 36.48, 25.30, 11.30]
errors = observed .- predicted
rmse = sqrt(sum(errors .^ 2) / length(errors))
mae = sum(abs.(errors)) / length(errors)
println("rmse=", round(rmse, digits=4))
println("mae=", round(mae, digits=4))
