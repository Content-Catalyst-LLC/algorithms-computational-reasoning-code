args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2) {
  stop("Usage: Rscript causal_effect_calculator.R <treated_mean> <control_mean>")
}
treated_mean <- as.numeric(args[1])
control_mean <- as.numeric(args[2])
cat(sprintf("treated_mean=%.6f\n", treated_mean))
cat(sprintf("control_mean=%.6f\n", control_mean))
cat(sprintf("difference=%.6f\n", treated_mean - control_mean))
