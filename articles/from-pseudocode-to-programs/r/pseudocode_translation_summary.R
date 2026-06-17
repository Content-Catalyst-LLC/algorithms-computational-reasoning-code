data <- read.csv("data/synthetic_pseudocode_translation_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["intent_clarity"]] +
    0.10 * row[["input_specification"]] +
    0.10 * row[["output_specification"]] +
    0.10 * row[["state_handling"]] +
    0.12 * row[["control_flow_fidelity"]] +
    0.10 * row[["edge_case_coverage"]] +
    0.10 * row[["error_handling"]] +
    0.10 * row[["test_coverage"]] +
    0.08 * row[["readability"]] +
    0.08 * row[["maintainability"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["intent_clarity"]],
    1 - row[["input_specification"]],
    1 - row[["output_specification"]],
    1 - row[["control_flow_fidelity"]],
    1 - row[["edge_case_coverage"]],
    1 - row[["error_handling"]],
    1 - row[["test_coverage"]],
    1 - row[["maintainability"]]
  ))
}

data$translation_quality <- apply(data, 1, quality_score)
data$translation_risk <- apply(data, 1, risk_score)
data$diagnostic <- ifelse(
  data$translation_quality >= 80 & data$translation_risk <= 25,
  "strong translation",
  ifelse(data$translation_risk >= 55, "high translation risk", "review needed")
)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_pseudocode_translation_summary.csv", row.names = FALSE)

png("outputs/figures/r_pseudocode_translation_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$translation_quality, data$translation_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Translation quality", "Translation risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Pseudocode Translation Quality vs. Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
