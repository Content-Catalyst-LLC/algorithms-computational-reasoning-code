data <- read.csv("data/synthetic_boundary_state_cases.csv", stringsAsFactors = FALSE)

score <- function(row) {
  100 * (
    0.12 * row[["input_clarity"]] +
    0.12 * row[["output_clarity"]] +
    0.12 * row[["state_definition"]] +
    0.10 * row[["transition_clarity"]] +
    0.12 * row[["stopping_condition_clarity"]] +
    0.10 * row[["validation_quality"]] +
    0.08 * row[["edge_case_handling"]] +
    0.08 * row[["failure_reporting"]] +
    0.08 * row[["interpretability"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk <- function(row) {
  100 * mean(c(
    1 - row[["input_clarity"]],
    1 - row[["output_clarity"]],
    1 - row[["state_definition"]],
    1 - row[["stopping_condition_clarity"]],
    1 - row[["edge_case_handling"]],
    1 - row[["failure_reporting"]],
    1 - row[["interpretability"]],
    1 - row[["governance_readiness"]]
  ))
}

data$boundary_score <- apply(data, 1, score)
data$boundary_risk <- apply(data, 1, risk)
data$diagnostic <- ifelse(
  data$boundary_score >= 80 & data$boundary_risk <= 25,
  "strong boundary specification",
  ifelse(data$boundary_risk >= 55, "high boundary risk", "review needed")
)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_boundary_state_summary.csv", row.names = FALSE)

png("outputs/figures/r_boundary_score_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$boundary_score, data$boundary_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Boundary score", "Boundary risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Boundary Score vs. Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
