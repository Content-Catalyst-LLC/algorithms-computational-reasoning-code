# Base R workflow for summarizing multi-objective optimization and trade-off audits.

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

audit_path <- file.path(tables_dir, "multi_objective_tradeoff_governance_audit.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

data <- read.csv(audit_path, stringsAsFactors = FALSE)

summary_table <- data.frame(
  case_count = nrow(data),
  average_tradeoff_governance_score = mean(data$tradeoff_governance_score),
  average_tradeoff_governance_risk = mean(data$tradeoff_governance_risk),
  highest_score_case = data$case_name[which.max(data$tradeoff_governance_score)],
  highest_risk_case = data$case_name[which.max(data$tradeoff_governance_risk)]
)

write.csv(summary_table, file.path(tables_dir, "r_multi_objective_tradeoff_governance_summary.csv"), row.names = FALSE)

comparison_matrix <- rbind(
  data$tradeoff_governance_score,
  data$tradeoff_governance_risk
)

colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c("Trade-off governance score", "Trade-off governance risk")

png(file.path(figures_dir, "tradeoff_governance_score_vs_risk.png"), width = 1500, height = 850)
barplot(comparison_matrix, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Trade-Off Governance Score vs. Risk")
legend("topleft", legend = rownames(comparison_matrix), pch = 15, bty = "n")
grid()
dev.off()

pareto_path <- file.path(tables_dir, "multi_objective_pareto_analysis.csv")

if (file.exists(pareto_path)) {
  pareto_data <- read.csv(pareto_path, stringsAsFactors = FALSE)
  write.csv(pareto_data, file.path(tables_dir, "r_multi_objective_pareto_analysis.csv"), row.names = FALSE)

  is_eff <- pareto_data$pareto_efficient == "True" | pareto_data$pareto_efficient == TRUE

  png(file.path(figures_dir, "pareto_cost_vs_service_quality.png"), width = 1400, height = 850)
  plot(pareto_data$cost, pareto_data$service_quality, pch = ifelse(is_eff, 19, 1), xlab = "Cost", ylab = "Service quality", main = "Cost vs. Service Quality with Pareto-Efficient Alternatives")
  text(pareto_data$cost, pareto_data$service_quality, labels = pareto_data$alternative, pos = 3)
  grid()
  dev.off()

  png(file.path(figures_dir, "pareto_emissions_vs_robustness.png"), width = 1400, height = 850)
  plot(pareto_data$emissions, pareto_data$robustness, pch = ifelse(is_eff, 19, 1), xlab = "Emissions", ylab = "Robustness", main = "Emissions vs. Robustness with Pareto-Efficient Alternatives")
  text(pareto_data$emissions, pareto_data$robustness, labels = pareto_data$alternative, pos = 3)
  grid()
  dev.off()
}

weighted_path <- file.path(tables_dir, "multi_objective_weighted_scores.csv")

if (file.exists(weighted_path)) {
  weighted_data <- read.csv(weighted_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "multi_objective_weighted_scores.png"), width = 1400, height = 850)
  barplot(weighted_data$weighted_score, names.arg = weighted_data$alternative, ylim = c(0, 1), xlab = "Alternative", ylab = "Weighted score", main = "Weighted Scores Under Balanced Objective Weights")
  grid()
  dev.off()
}

print(summary_table)
