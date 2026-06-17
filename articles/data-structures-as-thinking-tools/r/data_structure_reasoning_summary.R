data <- read.csv("data/synthetic_data_structure_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["operation_fit"]] +
    0.12 * row[["structural_fidelity"]] +
    0.10 * row[["invariant_clarity"]] +
    0.10 * row[["complexity_awareness"]] +
    0.08 * row[["memory_awareness"]] +
    0.10 * row[["interpretability"]] +
    0.10 * row[["retrieval_support"]] +
    0.08 * row[["transformation_support"]] +
    0.10 * row[["representation_risk_documentation"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["operation_fit"]],
    1 - row[["structural_fidelity"]],
    1 - row[["invariant_clarity"]],
    1 - row[["complexity_awareness"]],
    1 - row[["interpretability"]],
    1 - row[["retrieval_support"]],
    1 - row[["representation_risk_documentation"]],
    1 - row[["governance_readiness"]]
  ))
}

data$structure_reasoning_quality <- apply(data, 1, quality_score)
data$structure_mismatch_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_data_structure_reasoning_summary.csv", row.names = FALSE)

png("outputs/figures/r_data_structure_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$structure_reasoning_quality, data$structure_mismatch_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Structure-reasoning quality", "Structure-mismatch risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Data Structure Reasoning Quality vs. Structure-Mismatch Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
