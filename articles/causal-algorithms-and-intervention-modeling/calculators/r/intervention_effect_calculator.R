args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) stop("Usage: Rscript intervention_effect_calculator.R <baseline_outcome> <intervention_outcome>")
baseline <- as.numeric(args[1])
intervention <- as.numeric(args[2])
effect <- intervention - baseline
cat(sprintf("baseline_outcome=%.6f\n", baseline))
cat(sprintf("intervention_outcome=%.6f\n", intervention))
cat(sprintf("estimated_effect=%.6f\n", effect))
