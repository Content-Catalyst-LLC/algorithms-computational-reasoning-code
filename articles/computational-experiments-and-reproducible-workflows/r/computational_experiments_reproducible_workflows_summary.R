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

scenario_path <- file.path(tables_dir, "scenario_experiment_summaries.csv")
if (!file.exists(scenario_path)) {
  stop(paste("Missing", scenario_path, "Run the Python workflow first."))
}

scenario_data <- read.csv(scenario_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "scenario_estimated_effects.png"), width = 1300, height = 850)
barplot(scenario_data$estimated_effect, names.arg = scenario_data$scenario, las = 2,
        ylab = "Estimated effect", main = "Scenario Estimated Effects")
grid()
dev.off()

png(file.path(figures_dir, "scenario_threshold_rates.png"), width = 1300, height = 850)
barplot(scenario_data$threshold_rate, names.arg = scenario_data$scenario, las = 2,
        ylab = "Threshold rate", main = "Scenario Threshold Rates")
grid()
dev.off()

sensitivity_path <- file.path(tables_dir, "sensitivity_experiment_summary.csv")
if (file.exists(sensitivity_path)) {
  sensitivity_data <- read.csv(sensitivity_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "sensitivity_effect_response.png"), width = 1300, height = 850)
  plot(sensitivity_data$treatment_effect_parameter, sensitivity_data$mean_estimated_effect,
       type = "b", pch = 19, xlab = "Treatment effect parameter",
       ylab = "Mean estimated effect", main = "Sensitivity Response Across Effect Parameters")
  grid()
  dev.off()
}

checklist_path <- file.path(tables_dir, "reproducible_workflow_checklist.csv")
if (file.exists(checklist_path)) {
  checklist_data <- read.csv(checklist_path, stringsAsFactors = FALSE)
  status_counts <- table(checklist_data$status)
  png(file.path(figures_dir, "reproducible_workflow_checklist_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count",
          main = "Reproducible Workflow Checklist Status")
  grid()
  dev.off()
}

manifest_path <- file.path(tables_dir, "output_manifest.csv")
if (file.exists(manifest_path)) {
  manifest_data <- read.csv(manifest_path, stringsAsFactors = FALSE)
  manifest_summary <- data.frame(
    manifest_files = nrow(manifest_data),
    total_manifest_bytes = sum(manifest_data$size_bytes),
    largest_file = manifest_data$relative_path[which.max(manifest_data$size_bytes)]
  )
  write.csv(manifest_summary, file.path(tables_dir, "r_output_manifest_summary.csv"), row.names = FALSE)
}

summary_path <- file.path(tables_dir, "reproducible_experiment_audit_summary.csv")
summary_data <- read.csv(summary_path, stringsAsFactors = FALSE)

r_summary <- data.frame(
  workflow_summary_rows = nrow(summary_data),
  scenario_count = summary_data$scenario_count[1],
  synthetic_data_rows = summary_data$synthetic_data_rows[1],
  manifest_files = summary_data$manifest_files[1],
  review_items_needing_attention = summary_data$review_items_needing_attention[1]
)

write.csv(r_summary, file.path(tables_dir, "r_reproducible_workflow_summary.csv"), row.names = FALSE)
print(r_summary)
