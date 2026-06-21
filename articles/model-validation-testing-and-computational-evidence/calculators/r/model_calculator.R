observed <- c(33.1, 39.7, 38.8, 39.3, 8.4)
predicted <- c(31.92, 31.58, 36.48, 25.30, 11.30)
errors <- observed - predicted
rmse <- sqrt(mean(errors ^ 2))
mae <- mean(abs(errors))
bias <- mean(errors)
cat(sprintf("rmse=%.6f\n", rmse))
cat(sprintf("mae=%.6f\n", mae))
cat(sprintf("bias=%.6f\n", bias))
