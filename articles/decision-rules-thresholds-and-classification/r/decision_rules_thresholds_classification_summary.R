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

audit_path <- file.path(tables_dir, "decision_rules_thresholds_classification_audit.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

data <- read.csv(audit_path, stringsAsFactors = FALSE)

summary_table <- data.frame(
  case_count = nrow(data),
  average_classification_governance_score = mean(data$classification_governance_score),
  average_classification_governance_risk = mean(data$classification_governance_risk),
  highest_score_case = data$case_name[which.max(data$classification_governance_score)],
  highest_risk_case = data$case_name[which.max(data$classification_governance_risk)]
)

write.csv(
  summary_table,
  file.path(tables_dir, "r_decision_rules_thresholds_classification_summary.csv"),
  row.names = FALSE
)

comparison_matrix <- rbind(
  data$classification_governance_score,
  data$classification_governance_risk
)

colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c(
  "Classification governance score",
  "Classification governance risk"
)

png(
  file.path(figures_dir, "classification_governance_score_vs_risk.png"),
  width = 1500,
  height = 850
)

barplot(
  comparison_matrix,
  beside = TRUE,
  las = 2,
  ylim = c(0, 100),
  ylab = "Score",
  main = "Classification Governance Score vs. Risk"
)

legend(
  "topleft",
  legend = rownames(comparison_matrix),
  pch = 15,
  bty = "n"
)

grid()
dev.off()

threshold_path <- file.path(tables_dir, "decision_rules_thresholds_classification_threshold_examples.csv")

if (file.exists(threshold_path)) {
  thresholds <- read.csv(threshold_path, stringsAsFactors = FALSE)
  write.csv(
    thresholds,
    file.path(tables_dir, "r_decision_rules_thresholds_classification_threshold_examples.csv"),
    row.names = FALSE
  )
}

print(summary_table)
