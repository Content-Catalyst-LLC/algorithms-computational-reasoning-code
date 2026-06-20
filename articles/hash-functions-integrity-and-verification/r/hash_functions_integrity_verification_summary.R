# Base R workflow for summarizing hash verification and integrity audits.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

setwd(article_root)

tables_dir <- file.path(article_root, "outputs", "tables")
figures_dir <- file.path(article_root, "outputs", "figures")

if (!dir.exists(tables_dir)) dir.create(tables_dir, recursive = TRUE)
if (!dir.exists(figures_dir)) dir.create(figures_dir, recursive = TRUE)

audit_path <- file.path(tables_dir, "hash_verification_governance_audit.csv")
if (!file.exists(audit_path)) stop(paste("Missing", audit_path, "Run the Python workflow first."))

data <- read.csv(audit_path, stringsAsFactors = FALSE)

summary_table <- data.frame(
  case_count = nrow(data),
  average_hash_verification_score = mean(data$hash_verification_score),
  average_hash_verification_risk = mean(data$hash_verification_risk),
  highest_score_case = data$case_name[which.max(data$hash_verification_score)],
  highest_risk_case = data$case_name[which.max(data$hash_verification_risk)]
)

write.csv(summary_table, file.path(tables_dir, "r_hash_verification_governance_summary.csv"), row.names = FALSE)

comparison_matrix <- rbind(data$hash_verification_score, data$hash_verification_risk)
colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c("Hash verification score", "Hash verification risk")

png(file.path(figures_dir, "hash_verification_score_vs_risk.png"), width = 1500, height = 850)
barplot(comparison_matrix, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Hash Verification Governance Score vs. Risk")
legend("topleft", legend = rownames(comparison_matrix), pch = 15, bty = "n")
grid()
dev.off()

verification_path <- file.path(tables_dir, "hash_verification_results.csv")
if (file.exists(verification_path)) {
  verification_data <- read.csv(verification_path, stringsAsFactors = FALSE)
  write.csv(verification_data, file.path(tables_dir, "r_hash_verification_results.csv"), row.names = FALSE)
  verified_counts <- table(verification_data$sha256_verified)
  png(file.path(figures_dir, "sha256_verification_counts.png"), width = 1200, height = 800)
  barplot(verified_counts, ylim = c(0, max(verified_counts) + 1), ylab = "Count", main = "SHA-256 Verification Outcomes")
  grid()
  dev.off()
}

manifest_path <- file.path(tables_dir, "hash_manifest.csv")
if (file.exists(manifest_path)) {
  manifest_data <- read.csv(manifest_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "manifest_artifact_sizes.png"), width = 1300, height = 800)
  barplot(manifest_data$size_bytes, names.arg = manifest_data$file_name, las = 2, ylab = "Size in bytes", main = "Synthetic Manifest Artifact Sizes")
  grid()
  dev.off()
}

print(summary_table)
