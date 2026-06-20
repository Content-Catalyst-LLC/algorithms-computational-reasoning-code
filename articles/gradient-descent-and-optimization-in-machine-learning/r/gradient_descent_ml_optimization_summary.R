# Base R workflow for summarizing gradient descent and ML optimization audits.

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

audit_path <- file.path(tables_dir, "gradient_descent_ml_optimization_audit.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

data <- read.csv(audit_path, stringsAsFactors = FALSE)

summary_table <- data.frame(
  case_count = nrow(data),
  average_ml_optimization_governance_score = mean(data$ml_optimization_governance_score),
  average_ml_optimization_governance_risk = mean(data$ml_optimization_governance_risk),
  highest_score_case = data$case_name[which.max(data$ml_optimization_governance_score)],
  highest_risk_case = data$case_name[which.max(data$ml_optimization_governance_risk)]
)

write.csv(
  summary_table,
  file.path(tables_dir, "r_gradient_descent_ml_optimization_summary.csv"),
  row.names = FALSE
)

comparison_matrix <- rbind(
  data$ml_optimization_governance_score,
  data$ml_optimization_governance_risk
)

colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c(
  "ML optimization governance score",
  "ML optimization governance risk"
)

png(
  file.path(figures_dir, "ml_optimization_governance_score_vs_risk.png"),
  width = 1500,
  height = 850
)

barplot(
  comparison_matrix,
  beside = TRUE,
  las = 2,
  ylim = c(0, 100),
  ylab = "Score",
  main = "Machine Learning Optimization Governance Score vs. Risk"
)

legend(
  "topleft",
  legend = rownames(comparison_matrix),
  pch = 15,
  bty = "n"
)

grid()
dev.off()

trace_path <- file.path(tables_dir, "gradient_descent_training_trace.csv")

if (file.exists(trace_path)) {
  trace_data <- read.csv(trace_path, stringsAsFactors = FALSE)

  png(
    file.path(figures_dir, "gradient_descent_loss_trace.png"),
    width = 1400,
    height = 850
  )

  plot(
    trace_data$step,
    trace_data$loss,
    type = "l",
    xlab = "Training step",
    ylab = "Loss",
    main = "Gradient Descent Loss Trace"
  )

  points(trace_data$step, trace_data$loss, pch = 16)
  grid()
  dev.off()
}

print(summary_table)
