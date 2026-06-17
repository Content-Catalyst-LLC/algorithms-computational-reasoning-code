data <- read.csv("data/synthetic_formalization_cases.csv", stringsAsFactors = FALSE)

score <- function(row) {
  100 * (
    0.10 * row[["input_clarity"]] +
    0.10 * row[["output_clarity"]] +
    0.10 * row[["constraint_clarity"]] +
    0.08 * row[["state_definition"]] +
    0.14 * row[["objective_alignment"]] +
    0.12 * row[["assumption_documentation"]] +
    0.10 * row[["edge_case_handling"]] +
    0.08 * row[["stopping_condition_clarity"]] +
    0.10 * row[["evaluation_quality"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk <- function(row) {
  100 * mean(c(
    1 - row[["input_clarity"]],
    1 - row[["output_clarity"]],
    1 - row[["constraint_clarity"]],
    1 - row[["objective_alignment"]],
    1 - row[["assumption_documentation"]],
    1 - row[["edge_case_handling"]],
    1 - row[["evaluation_quality"]],
    1 - row[["governance_readiness"]]
  ))
}

data$formalization_score <- apply(data, 1, score)
data$formalization_risk <- apply(data, 1, risk)
data$diagnostic <- ifelse(
  data$formalization_score >= 80 & data$formalization_risk <= 25,
  "strong formalization",
  ifelse(data$formalization_risk >= 55, "high formalization risk", "review needed")
)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_formalization_summary.csv", row.names = FALSE)

png("outputs/figures/r_formalization_score_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$formalization_score, data$formalization_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Formalization score", "Formalization risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Formalization Score vs. Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
