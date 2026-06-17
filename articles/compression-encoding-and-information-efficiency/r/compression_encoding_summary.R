data <- read.csv("data/synthetic_compression_encoding_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["fidelity_requirement"]] +
    0.10 * row[["encoding_clarity"]] +
    0.10 * row[["compression_suitability"]] +
    0.10 * row[["metadata_preservation"]] +
    0.10 * row[["interoperability"]] +
    0.10 * row[["integrity_checks"]] +
    0.10 * row[["storage_efficiency"]] +
    0.08 * row[["transmission_efficiency"]] +
    0.10 * row[["accessibility_preservation"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["fidelity_requirement"]],
    1 - row[["encoding_clarity"]],
    1 - row[["metadata_preservation"]],
    1 - row[["interoperability"]],
    1 - row[["integrity_checks"]],
    1 - row[["accessibility_preservation"]],
    1 - row[["governance_readiness"]]
  ))
}

data$representation_quality <- apply(data, 1, quality_score)
data$representation_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_compression_encoding_summary.csv", row.names = FALSE)

png("outputs/figures/r_representation_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$representation_quality, data$representation_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Representation quality", "Representation risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Compression and Encoding Quality vs. Representation Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
