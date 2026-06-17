data <- read.csv("data/synthetic_programming_style_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["style_clarity"]] +
    0.10 * row[["state_visibility"]] +
    0.10 * row[["abstraction_fit"]] +
    0.10 * row[["composability"]] +
    0.10 * row[["testability"]] +
    0.10 * row[["error_handling"]] +
    0.10 * row[["traceability"]] +
    0.08 * row[["performance_fit"]] +
    0.10 * row[["team_readability"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["style_clarity"]],
    1 - row[["state_visibility"]],
    1 - row[["abstraction_fit"]],
    1 - row[["testability"]],
    1 - row[["error_handling"]],
    1 - row[["traceability"]],
    1 - row[["team_readability"]],
    1 - row[["governance_readiness"]]
  ))
}

data$style_quality <- apply(data, 1, quality_score)
data$style_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_programming_paradigm_style_summary.csv", row.names = FALSE)

png("outputs/figures/r_programming_style_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$style_quality, data$style_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Style quality", "Style risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Programming Style Quality vs. Style Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
