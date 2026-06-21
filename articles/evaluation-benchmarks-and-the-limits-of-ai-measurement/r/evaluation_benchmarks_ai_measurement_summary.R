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

summary_path <- file.path(tables_dir, "model_evaluation_summary.csv")
disagg_path <- file.path(tables_dir, "disaggregated_performance.csv")
audit_path <- file.path(tables_dir, "evaluation_audit_summary.csv")

if (!file.exists(summary_path)) {
  stop(paste("Missing", summary_path, "Run the Python workflow first."))
}

model_summary <- read.csv(summary_path, stringsAsFactors = FALSE)
disagg <- read.csv(disagg_path, stringsAsFactors = FALSE)
audit <- read.csv(audit_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "model_accuracy_and_calibration_gap.png"), width = 1100, height = 800)
score_matrix <- t(as.matrix(model_summary[, c("accuracy", "calibration_gap", "safety_flag_rate")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = model_summary$model,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Model Evaluation Summary")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.75,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "disaggregated_accuracy_by_group.png"), width = 1200, height = 850)
barplot(disagg$accuracy,
        names.arg = paste(disagg$model, disagg$group, sep = ": "),
        las = 2,
        ylim = c(0, 1),
        ylab = "Accuracy",
        main = "Disaggregated Accuracy by Group")
grid()
dev.off()

r_summary <- data.frame(
  models_reviewed = audit$models_reviewed[1],
  benchmark_items = audit$benchmark_items[1],
  models_requiring_review = audit$models_requiring_review[1],
  models_escalated = audit$models_escalated[1],
  saturated_models = audit$saturated_models[1],
  mean_accuracy = audit$mean_accuracy[1],
  mean_calibration_gap = audit$mean_calibration_gap[1],
  benchmark_limits_documented = audit$benchmark_limits_documented[1],
  contamination_checks_documented = audit$contamination_checks_documented[1],
  diagnostic_note = "AI evaluation should combine benchmark scores, calibration review, disaggregated performance, safety testing, contamination review, and deployment monitoring."
)

write.csv(r_summary, file.path(tables_dir, "r_evaluation_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
