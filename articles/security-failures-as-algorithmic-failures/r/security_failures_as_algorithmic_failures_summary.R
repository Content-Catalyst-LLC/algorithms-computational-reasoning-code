# security_failures_as_algorithmic_failures_summary.R
# Base R workflow for summarizing security failure pattern audits.

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

audit_path <- file.path(tables_dir, "security_failure_pattern_audit.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

data <- read.csv(audit_path, stringsAsFactors = FALSE)

summary_table <- data.frame(
  case_count = nrow(data),
  average_failure_resistance_score = mean(data$failure_resistance_score),
  average_algorithmic_failure_risk = mean(data$algorithmic_failure_risk),
  highest_risk_case = data$case_name[which.max(data$algorithmic_failure_risk)],
  strongest_case = data$case_name[which.max(data$failure_resistance_score)]
)

write.csv(
  summary_table,
  file.path(tables_dir, "r_security_failure_summary.csv"),
  row.names = FALSE
)

comparison_matrix <- rbind(
  data$failure_resistance_score,
  data$algorithmic_failure_risk
)

colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c(
  "Failure resistance score",
  "Algorithmic failure risk"
)

png(
  file.path(figures_dir, "failure_resistance_vs_algorithmic_failure_risk.png"),
  width = 1500,
  height = 850
)

barplot(
  comparison_matrix,
  beside = TRUE,
  las = 2,
  ylim = c(0, 100),
  ylab = "Score",
  main = "Security Failure Resistance vs. Algorithmic Failure Risk"
)

legend(
  "topleft",
  legend = rownames(comparison_matrix),
  pch = 15,
  bty = "n"
)

grid()
dev.off()

gap_path <- file.path(tables_dir, "control_gap_register.csv")

if (file.exists(gap_path)) {
  gap_data <- read.csv(gap_path, stringsAsFactors = FALSE)

  gap_matrix <- rbind(
    gap_data$control_gap_score,
    gap_data$hidden_gap_score
  )

  colnames(gap_matrix) <- gap_data$control
  rownames(gap_matrix) <- c("Control gap", "Hidden gap")

  png(
    file.path(figures_dir, "security_control_gap_scores.png"),
    width = 1500,
    height = 850
  )

  barplot(
    gap_matrix,
    beside = TRUE,
    las = 2,
    ylim = c(0, max(gap_matrix) + 10),
    ylab = "Gap score",
    main = "Security Control Gap Scores"
  )

  legend("topleft", legend = rownames(gap_matrix), pch = 15, bty = "n")
  grid()
  dev.off()
}

incident_path <- file.path(tables_dir, "incident_timeline_review.csv")

if (file.exists(incident_path)) {
  incident_data <- read.csv(incident_path, stringsAsFactors = FALSE)

  timeline_matrix <- rbind(
    incident_data$response_gap_hours,
    incident_data$total_resolution_hours
  )

  colnames(timeline_matrix) <- incident_data$incident
  rownames(timeline_matrix) <- c("Response gap", "Total resolution")

  png(
    file.path(figures_dir, "incident_response_timeline_review.png"),
    width = 1500,
    height = 850
  )

  barplot(
    timeline_matrix,
    beside = TRUE,
    las = 2,
    ylab = "Hours",
    main = "Incident Response Timeline Review"
  )

  legend("topleft", legend = rownames(timeline_matrix), pch = 15, bty = "n")
  grid()
  dev.off()
}

stress_path <- file.path(tables_dir, "assumption_stress_tests.csv")

if (file.exists(stress_path)) {
  stress_data <- read.csv(stress_path, stringsAsFactors = FALSE)
  stress_counts <- table(stress_data$result)

  png(
    file.path(figures_dir, "assumption_stress_test_results.png"),
    width = 1000,
    height = 750
  )

  barplot(
    stress_counts,
    ylim = c(0, max(stress_counts) + 1),
    ylab = "Count",
    main = "Assumption Stress Test Results"
  )

  grid()
  dev.off()
}

print(summary_table)
