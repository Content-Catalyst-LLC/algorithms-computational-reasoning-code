args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) stop("Usage: Rscript generalization_gap_calculator.R <train_metric> <test_metric>")
train_metric <- as.numeric(args[1])
test_metric <- as.numeric(args[2])
cat(sprintf("train_metric=%.6f
", train_metric))
cat(sprintf("test_metric=%.6f
", test_metric))
cat(sprintf("generalization_gap=%.6f
", train_metric - test_metric))
