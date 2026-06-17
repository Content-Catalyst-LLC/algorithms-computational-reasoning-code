data <- read.csv("data/synthetic_lambda_expression_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.10 * row[["expression_clarity"]] +
    0.12 * row[["binding_safety"]] +
    0.12 * row[["substitution_discipline"]] +
    0.10 * row[["reduction_traceability"]] +
    0.10 * row[["evaluation_strategy_clarity"]] +
    0.08 * row[["recursion_awareness"]] +
    0.12 * row[["type_discipline_clarity"]] +
    0.08 * row[["proof_connection"]] +
    0.08 * row[["implementation_relevance"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["binding_safety"]],
    1 - row[["substitution_discipline"]],
    1 - row[["reduction_traceability"]],
    1 - row[["evaluation_strategy_clarity"]],
    1 - row[["recursion_awareness"]],
    1 - row[["type_discipline_clarity"]],
    1 - row[["proof_connection"]],
    1 - row[["governance_readiness"]]
  ))
}

data$lambda_reasoning_quality <- apply(data, 1, quality_score)
data$formalization_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_lambda_expression_summary.csv", row.names = FALSE)

png("outputs/figures/r_lambda_reasoning_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$lambda_reasoning_quality, data$formalization_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Lambda-reasoning quality", "Formalization risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Lambda Reasoning Quality vs. Formalization Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
