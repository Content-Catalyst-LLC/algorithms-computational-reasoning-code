data <- read.csv("data/synthetic_verification_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["specification_clarity"]] +
    0.10 * row[["precondition_definition"]] +
    0.10 * row[["postcondition_definition"]] +
    0.12 * row[["invariant_coverage"]] +
    0.10 * row[["termination_evidence"]] +
    0.10 * row[["test_coverage"]] +
    0.10 * row[["counterexample_handling"]] +
    0.08 * row[["static_check_support"]] +
    0.10 * row[["traceability"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["specification_clarity"]],
    1 - row[["precondition_definition"]],
    1 - row[["postcondition_definition"]],
    1 - row[["invariant_coverage"]],
    1 - row[["termination_evidence"]],
    1 - row[["test_coverage"]],
    1 - row[["counterexample_handling"]],
    1 - row[["traceability"]]
  ))
}

data$verification_quality <- apply(data, 1, quality_score)
data$verification_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_algorithmic_verification_summary.csv", row.names = FALSE)

png("outputs/figures/r_verification_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$verification_quality, data$verification_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Verification quality", "Verification risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Verification Quality vs. Verification Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
