data <- read.csv("data/synthetic_reasoning_profiles.csv", stringsAsFactors = FALSE)

algorithmic_score <- function(row) {
  100 * (
    0.28 * row[["step_clarity"]] +
    0.24 * row[["decomposition"]] +
    0.24 * row[["control_flow"]] +
    0.24 * row[["testability"]]
  )
}

computational_score <- function(row) {
  100 * (
    0.11 * row[["step_clarity"]] +
    0.10 * row[["decomposition"]] +
    0.09 * row[["control_flow"]] +
    0.10 * row[["testability"]] +
    0.13 * row[["representation_quality"]] +
    0.12 * row[["data_context"]] +
    0.11 * row[["complexity_awareness"]] +
    0.12 * row[["interpretability"]] +
    0.12 * row[["governance_readiness"]] +
    0.10 * row[["stakeholder_awareness"]]
  )
}

data$algorithmic_thinking_score <- apply(data, 1, algorithmic_score)
data$computational_reasoning_score <- apply(data, 1, computational_score)
data$reasoning_gap <- data$computational_reasoning_score - data$algorithmic_thinking_score
data$diagnostic <- ifelse(
  data$reasoning_gap >= 15,
  "computational framing stronger",
  ifelse(data$reasoning_gap <= -15, "procedural design stronger", "balanced or mixed")
)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_reasoning_summary.csv", row.names = FALSE)

png("outputs/figures/r_reasoning_gap_by_scenario.png", width = 1400, height = 800)
barplot(data$reasoning_gap, names.arg = data$name, las = 2, ylab = "Computational minus algorithmic score", main = "Reasoning Gap by Scenario")
abline(h = 0, lty = 2)
grid()
dev.off()

print(data)
