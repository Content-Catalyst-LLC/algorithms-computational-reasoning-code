data <- read.csv("data/synthetic_debugging_reasoning_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["reproducibility"]] +
    0.10 * row[["expected_behavior_clarity"]] +
    0.10 * row[["trace_quality"]] +
    0.10 * row[["hypothesis_strength"]] +
    0.10 * row[["isolation_quality"]] +
    0.10 * row[["edge_case_awareness"]] +
    0.12 * row[["fix_verification"]] +
    0.10 * row[["regression_testing"]] +
    0.08 * row[["documentation_quality"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["reproducibility"]],
    1 - row[["expected_behavior_clarity"]],
    1 - row[["trace_quality"]],
    1 - row[["isolation_quality"]],
    1 - row[["edge_case_awareness"]],
    1 - row[["fix_verification"]],
    1 - row[["regression_testing"]],
    1 - row[["documentation_quality"]]
  ))
}

data$debugging_quality <- apply(data, 1, quality_score)
data$recurrence_risk <- apply(data, 1, risk_score)
data$diagnostic <- ifelse(
  data$debugging_quality >= 80 & data$recurrence_risk <= 25,
  "strong debugging process",
  ifelse(data$recurrence_risk >= 55, "high recurrence risk", "review needed")
)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_debugging_reasoning_summary.csv", row.names = FALSE)

png("outputs/figures/r_debugging_quality_vs_recurrence_risk.png", width = 1400, height = 800)
comparison <- rbind(data$debugging_quality, data$recurrence_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Debugging quality", "Recurrence risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Debugging Quality vs. Recurrence Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
