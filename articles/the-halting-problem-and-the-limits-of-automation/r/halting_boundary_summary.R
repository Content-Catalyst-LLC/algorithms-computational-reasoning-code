data <- read.csv("data/synthetic_halting_boundary_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.10 * row[["program_scope_clarity"]] +
    0.12 * row[["termination_claim_clarity"]] +
    0.12 * row[["undecidability_awareness"]] +
    0.10 * row[["bounded_analysis_honesty"]] +
    0.10 * row[["unknown_status_handling"]] +
    0.08 * row[["timeout_policy"]] +
    0.12 * row[["false_certainty_risk_control"]] +
    0.10 * row[["human_review_pathway"]] +
    0.08 * row[["traceability"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["termination_claim_clarity"]],
    1 - row[["undecidability_awareness"]],
    1 - row[["bounded_analysis_honesty"]],
    1 - row[["unknown_status_handling"]],
    1 - row[["false_certainty_risk_control"]],
    1 - row[["human_review_pathway"]],
    1 - row[["traceability"]],
    1 - row[["governance_readiness"]]
  ))
}

data$halting_boundary_quality <- apply(data, 1, quality_score)
data$automation_overclaim_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_halting_boundary_summary.csv", row.names = FALSE)

png("outputs/figures/r_halting_boundary_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$halting_boundary_quality, data$automation_overclaim_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Halting-boundary quality", "Automation-overclaim risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Halting Boundary Quality vs. Automation Overclaim Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
