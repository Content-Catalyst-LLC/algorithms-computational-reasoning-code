data <- read.csv("data/synthetic_sequence_structure_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["operation_fit"]] +
    0.12 * row[["order_semantics"]] +
    0.10 * row[["invariant_clarity"]] +
    0.10 * row[["complexity_awareness"]] +
    0.08 * row[["memory_behavior"]] +
    0.08 * row[["overflow_handling"]] +
    0.10 * row[["interpretability"]] +
    0.10 * row[["traversal_support"]] +
    0.10 * row[["representation_risk_documentation"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["operation_fit"]],
    1 - row[["order_semantics"]],
    1 - row[["invariant_clarity"]],
    1 - row[["complexity_awareness"]],
    1 - row[["overflow_handling"]],
    1 - row[["interpretability"]],
    1 - row[["representation_risk_documentation"]],
    1 - row[["governance_readiness"]]
  ))
}

data$sequence_structure_quality <- apply(data, 1, quality_score)
data$sequence_structure_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_sequence_structure_summary.csv", row.names = FALSE)

png("outputs/figures/r_sequence_structure_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$sequence_structure_quality, data$sequence_structure_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Sequence-structure quality", "Sequence-structure risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Sequence Structure Quality vs. Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
