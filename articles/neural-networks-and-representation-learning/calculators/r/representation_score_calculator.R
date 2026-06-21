args <- commandArgs(trailingOnly = TRUE)
values <- as.numeric(args)
if (length(values) < 4) {
  stop("Usage: Rscript representation_score_calculator.R x1 x2 x3 bias")
}
x1 <- values[1]
x2 <- values[2]
x3 <- values[3]
bias <- values[4]
linear <- 0.9 * x1 - 0.7 * x2 + 0.35 * x3 + bias
score <- 1 / (1 + exp(-linear))
cat(sprintf("linear_signal=%.6f\n", linear))
cat(sprintf("representation_score=%.6f\n", score))
