train_error = 0.04
test_error = 0.09
println("generalization_gap=", round(test_error - train_error, digits=4))
