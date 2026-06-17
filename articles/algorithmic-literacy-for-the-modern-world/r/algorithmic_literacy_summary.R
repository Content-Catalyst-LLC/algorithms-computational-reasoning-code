data <- read.csv("data/synthetic_algorithmic_literacy_cases.csv", stringsAsFactors = FALSE)

support_score <- function(row) {
  100 * (
    0.14 * row[["procedural_transparency"]] +
    0.12 * row[["data_visibility"]] +
    0.14 * row[["output_interpretability"]] +
    0.12 * row[["uncertainty_communication"]] +
    0.12 * row[["contestability"]] +
    0.12 * row[["governance_readiness"]] +
    0.12 * row[["impact_awareness"]] +
    0.12 * row[["human_judgment_support"]]
  )
}

gap_score <- function(row) {
  100 * mean(c(
    1 - row[["procedural_transparency"]],
    1 - row[["data_visibility"]],
    1 - row[["output_interpretability"]],
    1 - row[["uncertainty_communication"]],
    1 - row[["contestability"]],
    1 - row[["governance_readiness"]],
    1 - row[["impact_awareness"]],
    1 - row[["human_judgment_support"]]
  ))
}

data$literacy_support_score <- apply(data, 1, support_score)
data$literacy_gap_score <- apply(data, 1, gap_score)
data$diagnostic <- ifelse(
  data$literacy_support_score >= 80 & data$literacy_gap_score <= 25,
  "strong literacy support",
  ifelse(data$literacy_gap_score >= 55, "high literacy gap", "review needed")
)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_algorithmic_literacy_summary.csv", row.names = FALSE)

png("outputs/figures/r_algorithmic_literacy_support_vs_gap.png", width = 1400, height = 800)
comparison <- rbind(data$literacy_support_score, data$literacy_gap_score)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Literacy support", "Literacy gap")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Algorithmic Literacy Support vs. Gap")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
