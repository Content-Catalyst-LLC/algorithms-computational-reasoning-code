train_accuracy = 0.88
test_accuracy = 0.81
println("generalization_gap=", round(train_accuracy - test_accuracy, digits=4))
