args <- commandArgs(trailingOnly = TRUE)
values <- as.numeric(args)
if (length(values) < 2) stop("Usage: Rscript model_error_calculator.R <train_error> <test_error>")
train_error <- values[1]
test_error <- values[2]
gap <- test_error - train_error
cat(sprintf("train_error=%.6f\n", train_error))
cat(sprintf("test_error=%.6f\n", test_error))
cat(sprintf("generalization_gap=%.6f\n", gap))
