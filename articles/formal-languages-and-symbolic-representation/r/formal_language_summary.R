data <- read.csv("data/synthetic_formal_language_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.10 * row[["alphabet_clarity"]] +
    0.12 * row[["grammar_explicitness"]] +
    0.12 * row[["syntax_validation"]] +
    0.12 * row[["semantic_clarity"]] +
    0.10 * row[["parser_readiness"]] +
    0.10 * row[["schema_support"]] +
    0.10 * row[["error_reporting"]] +
    0.08 * row[["testability"]] +
    0.08 * row[["interoperability"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["alphabet_clarity"]],
    1 - row[["grammar_explicitness"]],
    1 - row[["syntax_validation"]],
    1 - row[["semantic_clarity"]],
    1 - row[["parser_readiness"]],
    1 - row[["schema_support"]],
    1 - row[["error_reporting"]],
    1 - row[["interoperability"]]
  ))
}

data$representation_quality <- apply(data, 1, quality_score)
data$representation_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_formal_language_summary.csv", row.names = FALSE)

png("outputs/figures/r_representation_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$representation_quality, data$representation_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Representation quality", "Representation risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Symbolic Representation Quality vs. Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
