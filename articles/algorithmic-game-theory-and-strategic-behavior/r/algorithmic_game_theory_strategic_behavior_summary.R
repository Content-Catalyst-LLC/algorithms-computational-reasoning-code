# Base R workflow for summarizing strategic behavior and mechanism audits.

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
audit_path <- file.path(tables_dir, "algorithmic_game_theory_strategic_governance_audit.csv")
if (!file.exists(audit_path)) stop(paste("Missing", audit_path, "Run the Python workflow first."))
data <- read.csv(audit_path, stringsAsFactors = FALSE)
summary_table <- data.frame(
  case_count = nrow(data),
  average_strategic_governance_score = mean(data$strategic_governance_score),
  average_strategic_governance_risk = mean(data$strategic_governance_risk),
  highest_score_case = data$case_name[which.max(data$strategic_governance_score)],
  highest_risk_case = data$case_name[which.max(data$strategic_governance_risk)]
)
write.csv(summary_table, file.path(tables_dir, "r_algorithmic_game_theory_strategic_governance_summary.csv"), row.names = FALSE)
comparison_matrix <- rbind(data$strategic_governance_score, data$strategic_governance_risk)
colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c("Strategic governance score", "Strategic governance risk")
png(file.path(figures_dir, "strategic_governance_score_vs_risk.png"), width = 1500, height = 850)
barplot(comparison_matrix, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Strategic Governance Score vs. Risk")
legend("topleft", legend = rownames(comparison_matrix), pch = 15, bty = "n")
grid()
dev.off()
sensitivity_path <- file.path(tables_dir, "incentive_sensitivity_examples.csv")
if (file.exists(sensitivity_path)) {
  sensitivity_data <- read.csv(sensitivity_path, stringsAsFactors = FALSE)
  write.csv(sensitivity_data, file.path(tables_dir, "r_incentive_sensitivity_examples.csv"), row.names = FALSE)
  png(file.path(figures_dir, "incentive_sensitivity_penalty_vs_net_gain.png"), width = 1400, height = 850)
  attractive <- sensitivity_data$manipulation_attractive == "True" | sensitivity_data$manipulation_attractive == TRUE
  plot(sensitivity_data$penalty, sensitivity_data$net_gain_from_manipulation, pch = ifelse(attractive, 19, 1), xlab = "Penalty", ylab = "Net gain from manipulation", main = "Incentive Sensitivity: Penalty vs. Manipulation Gain")
  abline(h = 0, lty = 2)
  grid()
  dev.off()
}
payoff_path <- file.path(tables_dir, "payoff_game_table.csv")
if (file.exists(payoff_path)) {
  payoff_data <- read.csv(payoff_path, stringsAsFactors = FALSE)
  labels <- paste(payoff_data$player_one_strategy, payoff_data$player_two_strategy, sep = " / ")
  png(file.path(figures_dir, "payoff_game_total_welfare.png"), width = 1400, height = 850)
  barplot(payoff_data$total_welfare, names.arg = labels, las = 2, ylab = "Total welfare", main = "Total Welfare Across Strategy Profiles")
  grid()
  dev.off()
}
print(summary_table)
