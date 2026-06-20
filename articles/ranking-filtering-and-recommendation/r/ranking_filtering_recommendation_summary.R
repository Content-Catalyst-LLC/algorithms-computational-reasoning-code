# Base R workflow for summarizing ranking, filtering, and recommendation audits.
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
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

audit_path <- file.path(tables_dir, "ranking_filtering_recommendation_audit.csv")
if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

data <- read.csv(audit_path, stringsAsFactors = FALSE)
summary_table <- data.frame(
  case_count = nrow(data),
  average_ranking_system_score = mean(data$ranking_system_score),
  average_ranking_system_risk = mean(data$ranking_system_risk),
  highest_score_case = data$case_name[which.max(data$ranking_system_score)],
  highest_risk_case = data$case_name[which.max(data$ranking_system_risk)]
)

write.csv(summary_table, file.path(tables_dir, "r_ranking_filtering_recommendation_summary.csv"), row.names = FALSE)
comparison_matrix <- rbind(data$ranking_system_score, data$ranking_system_risk)
colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c("Ranking system score", "Ranking system risk")

png(file.path(figures_dir, "ranking_system_score_vs_risk.png"), width = 1500, height = 850)
barplot(comparison_matrix, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Ranking System Score vs. Risk")
legend("topleft", legend = rownames(comparison_matrix), pch = 15, bty = "n")
grid()
dev.off()

print(summary_table)
