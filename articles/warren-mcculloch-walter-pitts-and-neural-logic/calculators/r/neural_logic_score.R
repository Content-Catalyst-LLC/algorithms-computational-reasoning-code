args <- commandArgs(trailingOnly = TRUE)
vals <- as.numeric(args)
if (length(vals) == 0) {
  vals <- c(0.96, 0.94, 0.96, 0.86, 0.96, 0.94, 0.98, 0.94, 0.98, 0.90)
}
cat(sprintf("neural_logic_score=%.6f\n", mean(vals)))
