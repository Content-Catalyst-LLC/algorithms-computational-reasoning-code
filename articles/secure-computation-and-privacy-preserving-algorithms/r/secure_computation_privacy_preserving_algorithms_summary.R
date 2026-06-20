# secure_computation_privacy_preserving_algorithms_summary.R
# Base R workflow for summarizing privacy-preserving computation audits.

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

audit_path <- file.path(tables_dir, "privacy_preserving_governance_audit.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

data <- read.csv(audit_path, stringsAsFactors = FALSE)

summary_table <- data.frame(
  case_count = nrow(data),
  average_privacy_governance_score = mean(data$privacy_governance_score),
  average_privacy_governance_risk = mean(data$privacy_governance_risk),
  highest_score_case = data$case_name[which.max(data$privacy_governance_score)],
  highest_risk_case = data$case_name[which.max(data$privacy_governance_risk)]
)

write.csv(
  summary_table,
  file.path(tables_dir, "r_privacy_preserving_governance_summary.csv"),
  row.names = FALSE
)

comparison_matrix <- rbind(
  data$privacy_governance_score,
  data$privacy_governance_risk
)

colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c(
  "Privacy governance score",
  "Privacy governance risk"
)

png(
  file.path(figures_dir, "privacy_governance_score_vs_risk.png"),
  width = 1500,
  height = 850
)

barplot(
  comparison_matrix,
  beside = TRUE,
  las = 2,
  ylim = c(0, 100),
  ylab = "Score",
  main = "Privacy-Preserving Computation Governance Score vs. Risk"
)

legend(
  "topleft",
  legend = rownames(comparison_matrix),
  pch = 15,
  bty = "n"
)

grid()
dev.off()

budget_path <- file.path(tables_dir, "privacy_budget_ledger.csv")

if (file.exists(budget_path)) {
  budget_data <- read.csv(budget_path, stringsAsFactors = FALSE)

  png(
    file.path(figures_dir, "privacy_budget_accumulation.png"),
    width = 1400,
    height = 850
  )

  plot(
    seq_len(nrow(budget_data)),
    budget_data$cumulative_epsilon,
    type = "b",
    xlab = "Release number",
    ylab = "Cumulative epsilon",
    main = "Privacy Budget Accumulation Across Releases",
    xaxt = "n"
  )

  axis(1, at = seq_len(nrow(budget_data)), labels = budget_data$release, las = 2)
  grid()
  dev.off()
}

risk_path <- file.path(tables_dir, "reidentification_risk_review.csv")

if (file.exists(risk_path)) {
  risk_data <- read.csv(risk_path, stringsAsFactors = FALSE)

  png(
    file.path(figures_dir, "reidentification_risk_scores.png"),
    width = 1400,
    height = 850
  )

  barplot(
    risk_data$reidentification_risk_score,
    names.arg = risk_data$group,
    las = 2,
    ylim = c(0, 100),
    ylab = "Risk score",
    main = "Re-Identification Risk Review"
  )

  grid()
  dev.off()
}

fed_path <- file.path(tables_dir, "federated_averaging_demo.csv")

if (file.exists(fed_path)) {
  fed_data <- read.csv(fed_path, stringsAsFactors = FALSE)
  client_data <- fed_data[fed_data$client != "global_model", ]

  png(
    file.path(figures_dir, "federated_client_weight_contributions.png"),
    width = 1400,
    height = 850
  )

  barplot(
    client_data$weighted_contribution,
    names.arg = client_data$client,
    ylim = c(0, max(client_data$weighted_contribution) + 0.1),
    ylab = "Weighted contribution",
    main = "Federated Averaging Contributions"
  )

  grid()
  dev.off()
}

dp_path <- file.path(tables_dir, "differential_privacy_count_demo.csv")

if (file.exists(dp_path)) {
  dp_data <- read.csv(dp_path, stringsAsFactors = FALSE)

  write.csv(
    dp_data,
    file.path(tables_dir, "r_differential_privacy_count_demo.csv"),
    row.names = FALSE
  )
}

print(summary_table)
