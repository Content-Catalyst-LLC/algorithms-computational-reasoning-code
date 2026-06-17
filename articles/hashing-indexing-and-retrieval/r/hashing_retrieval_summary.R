data <- read.csv("data/synthetic_hashing_retrieval_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["key_clarity"]] +
    0.08 * row[["hash_suitability"]] +
    0.10 * row[["collision_handling"]] +
    0.12 * row[["index_coverage"]] +
    0.10 * row[["retrieval_speed_fit"]] +
    0.10 * row[["freshness_control"]] +
    0.10 * row[["ranking_transparency"]] +
    0.10 * row[["metadata_provenance"]] +
    0.08 * row[["security_boundary_clarity"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["key_clarity"]],
    1 - row[["collision_handling"]],
    1 - row[["index_coverage"]],
    1 - row[["freshness_control"]],
    1 - row[["ranking_transparency"]],
    1 - row[["metadata_provenance"]],
    1 - row[["security_boundary_clarity"]],
    1 - row[["governance_readiness"]]
  ))
}

data$retrieval_quality <- apply(data, 1, quality_score)
data$retrieval_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_hashing_retrieval_summary.csv", row.names = FALSE)

png("outputs/figures/r_retrieval_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$retrieval_quality, data$retrieval_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Retrieval quality", "Retrieval risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Retrieval Quality vs. Retrieval Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
