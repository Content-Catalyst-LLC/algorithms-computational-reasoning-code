data <- read.csv("data/synthetic_formal_methods_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["specification_clarity"]] +
    0.10 * row[["assumption_documentation"]] +
    0.10 * row[["invariant_strength"]] +
    0.12 * row[["proof_obligation_traceability"]] +
    0.12 * row[["machine_check_status"]] +
    0.10 * row[["counterexample_handling"]] +
    0.10 * row[["model_scope_clarity"]] +
    0.08 * row[["refinement_evidence"]] +
    0.08 * row[["unknown_status_handling"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["specification_clarity"]],
    1 - row[["assumption_documentation"]],
    1 - row[["proof_obligation_traceability"]],
    1 - row[["machine_check_status"]],
    1 - row[["model_scope_clarity"]],
    1 - row[["refinement_evidence"]],
    1 - row[["unknown_status_handling"]],
    1 - row[["governance_readiness"]]
  ))
}

data$formal_methods_quality <- apply(data, 1, quality_score)
data$verification_overclaim_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_formal_methods_summary.csv", row.names = FALSE)

png("outputs/figures/r_formal_methods_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$formal_methods_quality, data$verification_overclaim_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Formal-methods quality", "Verification-overclaim risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Formal Methods Quality vs. Verification Overclaim Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
