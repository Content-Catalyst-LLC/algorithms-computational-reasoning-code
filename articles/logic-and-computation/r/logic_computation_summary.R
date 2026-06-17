data <- read.csv("data/synthetic_logic_computation_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["rule_clarity"]] +
    0.12 * row[["predicate_definition"]] +
    0.10 * row[["input_validity"]] +
    0.10 * row[["contradiction_control"]] +
    0.12 * row[["inference_traceability"]] +
    0.10 * row[["constraint_coverage"]] +
    0.10 * row[["testability"]] +
    0.08 * row[["verification_readiness"]] +
    0.08 * row[["explainability"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["rule_clarity"]],
    1 - row[["predicate_definition"]],
    1 - row[["input_validity"]],
    1 - row[["contradiction_control"]],
    1 - row[["inference_traceability"]],
    1 - row[["constraint_coverage"]],
    1 - row[["testability"]],
    1 - row[["explainability"]]
  ))
}

data$logic_quality <- apply(data, 1, quality_score)
data$logic_risk <- apply(data, 1, risk_score)
data$diagnostic <- ifelse(
  data$logic_quality >= 80 & data$logic_risk <= 25,
  "strong logical structure",
  ifelse(data$logic_risk >= 55, "high logic risk", "review needed")
)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_logic_computation_summary.csv", row.names = FALSE)

png("outputs/figures/r_logic_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$logic_quality, data$logic_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Logic quality", "Logic risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Logic Quality vs. Logic Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
