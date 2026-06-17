data <- read.csv("data/synthetic_execution_model_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.10 * row[["translation_clarity"]] +
    0.10 * row[["semantic_checking"]] +
    0.10 * row[["optimization_traceability"]] +
    0.10 * row[["runtime_visibility"]] +
    0.10 * row[["diagnostics_quality"]] +
    0.10 * row[["portability"]] +
    0.12 * row[["reproducibility"]] +
    0.12 * row[["security_boundaries"]] +
    0.08 * row[["performance_fit"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["translation_clarity"]],
    1 - row[["semantic_checking"]],
    1 - row[["optimization_traceability"]],
    1 - row[["runtime_visibility"]],
    1 - row[["diagnostics_quality"]],
    1 - row[["reproducibility"]],
    1 - row[["security_boundaries"]],
    1 - row[["governance_readiness"]]
  ))
}

data$execution_quality <- apply(data, 1, quality_score)
data$execution_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_execution_model_summary.csv", row.names = FALSE)

png("outputs/figures/r_execution_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$execution_quality, data$execution_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Execution quality", "Execution risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Execution Quality vs. Execution Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
