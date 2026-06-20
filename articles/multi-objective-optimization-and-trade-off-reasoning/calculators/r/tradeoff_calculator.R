# Self-contained R calculator for weighted-score trade-off reasoning.

out_dir <- file.path(getwd(), "calculators", "outputs")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

alternatives <- data.frame(
  alternative = c("A", "B", "C", "D"),
  cost = c(72, 64, 81, 58),
  risk = c(34, 41, 26, 52),
  service_quality = c(82, 76, 88, 69)
)

normalize_min <- function(x) if (max(x) == min(x)) rep(1, length(x)) else (max(x) - x) / (max(x) - min(x))
normalize_max <- function(x) if (max(x) == min(x)) rep(1, length(x)) else (x - min(x)) / (max(x) - min(x))

alternatives$weighted_score <- 0.35 * normalize_min(alternatives$cost) +
  0.30 * normalize_min(alternatives$risk) +
  0.35 * normalize_max(alternatives$service_quality)

alternatives <- alternatives[order(-alternatives$weighted_score), ]
write.csv(alternatives, file.path(out_dir, "r_tradeoff_calculator_weighted_scores.csv"), row.names = FALSE)
print(alternatives)
