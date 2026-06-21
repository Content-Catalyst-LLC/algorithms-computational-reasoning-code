args <- commandArgs(trailingOnly = TRUE)
values <- as.numeric(args)
if (length(values) != 4) stop("Usage: Rscript expected_value_calculator.R probability benefit loss cost")
p <- max(0, min(1, values[1]))
expected_value <- p * values[2] - p * values[3] - values[4]
cat(sprintf("probability=%.6f\n", p))
cat(sprintf("expected_value=%.6f\n", expected_value))
