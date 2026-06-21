# Compact Julia example: classification threshold and reward estimate.
probability = 0.62
threshold = 0.55
prediction = probability >= threshold ? 1 : 0
expected_reward = 0.54 * 1.0 - 0.08
println((prediction=prediction, expected_reward=expected_reward))
