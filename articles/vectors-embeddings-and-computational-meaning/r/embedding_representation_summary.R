data <- read.csv("data/synthetic_embedding_system_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["representation_fit"]] +
    0.10 * row[["model_documentation"]] +
    0.10 * row[["vector_compatibility"]] +
    0.10 * row[["similarity_interpretability"]] +
    0.10 * row[["retrieval_evidence"]] +
    0.10 * row[["metadata_provenance"]] +
    0.10 * row[["bias_review"]] +
    0.08 * row[["drift_monitoring"]] +
    0.10 * row[["access_boundary_clarity"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["representation_fit"]],
    1 - row[["model_documentation"]],
    1 - row[["similarity_interpretability"]],
    1 - row[["retrieval_evidence"]],
    1 - row[["metadata_provenance"]],
    1 - row[["bias_review"]],
    1 - row[["drift_monitoring"]],
    1 - row[["governance_readiness"]]
  ))
}

data$embedding_quality <- apply(data, 1, quality_score)
data$meaning_overclaim_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_embedding_representation_summary.csv", row.names = FALSE)

png("outputs/figures/r_embedding_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$embedding_quality, data$meaning_overclaim_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Embedding quality", "Meaning-overclaim risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Embedding Quality vs. Meaning-Overclaim Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
