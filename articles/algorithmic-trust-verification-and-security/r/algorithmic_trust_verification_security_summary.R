# algorithmic_trust_verification_security_summary.R
# Base R workflow for summarizing trust evidence, residual risk, and calibration.

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

if (!dir.exists(tables_dir)) {
  dir.create(tables_dir, recursive = TRUE)
}

if (!dir.exists(figures_dir)) {
  dir.create(figures_dir, recursive = TRUE)
}

audit_path <- file.path(tables_dir, "algorithmic_trust_audit.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

data <- read.csv(audit_path, stringsAsFactors = FALSE)

summary_table <- data.frame(
  case_count = nrow(data),
  average_trust_quality_score = mean(data$trust_quality_score),
  average_residual_trust_risk = mean(data$residual_trust_risk),
  highest_trust_quality_case = data$case_name[which.max(data$trust_quality_score)],
  highest_residual_risk_case = data$case_name[which.max(data$residual_trust_risk)]
)

write.csv(summary_table, file.path(tables_dir, "r_algorithmic_trust_summary.csv"), row.names = FALSE)

comparison_matrix <- rbind(data$trust_quality_score, data$residual_trust_risk)
colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c("Trust quality score", "Residual trust risk")

png(file.path(figures_dir, "trust_quality_score_vs_residual_risk.png"), width = 1500, height = 850)
barplot(comparison_matrix, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Algorithmic Trust Quality vs. Residual Risk")
legend("topleft", legend = rownames(comparison_matrix), pch = 15, bty = "n")
grid()
dev.off()

evidence_path <- file.path(tables_dir, "trust_evidence_coverage_matrix.csv")
if (file.exists(evidence_path)) {
  evidence_data <- read.csv(evidence_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "trust_evidence_average_coverage.png"), width = 1400, height = 850)
  barplot(evidence_data$average_coverage, names.arg = evidence_data$evidence, las = 2, ylim = c(0, 100), ylab = "Average coverage score", main = "Trust Evidence Coverage")
  grid()
  dev.off()
}

risk_path <- file.path(tables_dir, "residual_risk_register.csv")
if (file.exists(risk_path)) {
  risk_data <- read.csv(risk_path, stringsAsFactors = FALSE)
  risk_matrix <- rbind(risk_data$initial_risk_score, risk_data$residual_risk_score)
  colnames(risk_matrix) <- risk_data$risk
  rownames(risk_matrix) <- c("Initial risk", "Residual risk")
  png(file.path(figures_dir, "initial_vs_residual_risk.png"), width = 1400, height = 850)
  barplot(risk_matrix, beside = TRUE, las = 2, ylim = c(0, max(risk_matrix) + 10), ylab = "Risk score", main = "Initial Risk vs. Residual Risk")
  legend("topleft", legend = rownames(risk_matrix), pch = 15, bty = "n")
  grid()
  dev.off()
}

calibration_path <- file.path(tables_dir, "trust_calibration_review.csv")
if (file.exists(calibration_path)) {
  calibration_data <- read.csv(calibration_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "trust_calibration_gap.png"), width = 1300, height = 800)
  barplot(calibration_data$calibration_gap, names.arg = calibration_data$user_group, las = 2, ylim = c(0, max(calibration_data$calibration_gap) + 0.1), ylab = "Calibration gap", main = "Human Trust Calibration Gap")
  grid()
  dev.off()
}

print(summary_table)
