data <- read.csv("data/synthetic_decomposition_cases.csv", stringsAsFactors = FALSE)

score <- function(row) {
  100 * (
    0.12 * row[["subproblem_clarity"]] +
    0.10 * row[["boundary_definition"]] +
    0.10 * row[["input_output_clarity"]] +
    0.10 * row[["sequencing_quality"]] +
    0.10 * row[["dependency_visibility"]] +
    0.12 * row[["testability"]] +
    0.10 * row[["traceability"]] +
    0.10 * row[["recomposition_quality"]] +
    0.08 * row[["governance_readiness"]] +
    0.08 * row[["risk_awareness"]]
  )
}

risk <- function(row) {
  100 * mean(c(
    1 - row[["boundary_definition"]],
    1 - row[["dependency_visibility"]],
    1 - row[["traceability"]],
    1 - row[["recomposition_quality"]],
    1 - row[["governance_readiness"]],
    1 - row[["risk_awareness"]]
  ))
}

data$decomposition_score <- apply(data, 1, score)
data$decomposition_risk <- apply(data, 1, risk)
data$diagnostic <- ifelse(
  data$decomposition_score >= 80 & data$decomposition_risk <= 25,
  "strong decomposition",
  ifelse(data$decomposition_risk >= 55, "high decomposition risk", "review needed")
)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_decomposition_summary.csv", row.names = FALSE)

png("outputs/figures/r_decomposition_score_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$decomposition_score, data$decomposition_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Decomposition score", "Decomposition risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Decomposition Score vs. Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
