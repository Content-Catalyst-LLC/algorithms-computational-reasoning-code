data <- read.csv("data/synthetic_boundary_reliability_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["stopping_condition_clarity"]] +
    0.12 * row[["progress_measure_definition"]] +
    0.12 * row[["invariant_coverage"]] +
    0.10 * row[["boundary_case_coverage"]] +
    0.10 * row[["invalid_input_handling"]] +
    0.08 * row[["recursion_safety"]] +
    0.08 * row[["numerical_edge_handling"]] +
    0.08 * row[["concurrency_edge_awareness"]] +
    0.10 * row[["counterexample_traceability"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["stopping_condition_clarity"]],
    1 - row[["progress_measure_definition"]],
    1 - row[["invariant_coverage"]],
    1 - row[["boundary_case_coverage"]],
    1 - row[["invalid_input_handling"]],
    1 - row[["recursion_safety"]],
    1 - row[["numerical_edge_handling"]],
    1 - row[["counterexample_traceability"]]
  ))
}

data$reliability_quality <- apply(data, 1, quality_score)
data$reliability_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_termination_invariant_edge_summary.csv", row.names = FALSE)

png("outputs/figures/r_reliability_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$reliability_quality, data$reliability_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Reliability quality", "Reliability risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Termination, Invariant, and Edge-Case Reliability")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
