data <- read.csv("data/synthetic_automated_reasoning_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["formalization_clarity"]] +
    0.10 * row[["premise_quality"]] +
    0.12 * row[["rule_soundness"]] +
    0.12 * row[["inference_traceability"]] +
    0.10 * row[["proof_or_model_evidence"]] +
    0.08 * row[["satisfiability_handling"]] +
    0.10 * row[["counterexample_handling"]] +
    0.08 * row[["unknown_status_handling"]] +
    0.08 * row[["human_review_pathway"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["formalization_clarity"]],
    1 - row[["premise_quality"]],
    1 - row[["rule_soundness"]],
    1 - row[["inference_traceability"]],
    1 - row[["proof_or_model_evidence"]],
    1 - row[["unknown_status_handling"]],
    1 - row[["human_review_pathway"]],
    1 - row[["governance_readiness"]]
  ))
}

data$automated_reasoning_quality <- apply(data, 1, quality_score)
data$inference_overclaim_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_automated_reasoning_summary.csv", row.names = FALSE)

png("outputs/figures/r_automated_reasoning_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$automated_reasoning_quality, data$inference_overclaim_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Automated-reasoning quality", "Inference-overclaim risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Automated Reasoning Quality vs. Inference Overclaim Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
