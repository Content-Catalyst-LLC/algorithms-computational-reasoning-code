args <- commandArgs(trailingOnly = TRUE)
x <- as.numeric(args)
if (length(x) == 0) {
  x <- c(0.90,0.92,0.94,0.88,0.82,0.88,0.96,0.96,0.94,0.98)
}
cat(sprintf("philosophical_review_score=%.6f\n", mean(x)))
