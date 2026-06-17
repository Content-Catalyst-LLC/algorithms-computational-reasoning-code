data <- read.csv("data/synthetic_algorithm_scenarios.csv", stringsAsFactors = FALSE)

score <- function(row) {
  100 * (
    0.14 * row[["representation_quality"]] +
    0.10 * row[["indexing_strength"]] +
    0.10 * row[["decomposition_strength"]] +
    0.13 * row[["correctness_evidence"]] +
    0.09 * row[["interpretability"]] +
    0.09 * row[["robustness"]] +
    0.12 * row[["governance_readiness"]] +
    0.10 * row[["data_quality"]] +
    0.10 * row[["objective_alignment"]] +
    0.08 * row[["memory_efficiency"]] +
    0.05 * row[["monitoring_strength"]] -
    0.10 * row[["brute_force_pressure"]]
  )
}

data$algorithmic_reasoning_score <- apply(data, 1, score)
data$diagnostic <- ifelse(
  data$algorithmic_reasoning_score >= 70,
  "strong algorithmic reasoning profile",
  ifelse(data$algorithmic_reasoning_score >= 55, "partial profile with review needs", "weak profile requiring redesign")
)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_algorithmic_reasoning_summary.csv", row.names = FALSE)
print(data)
