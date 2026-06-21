# simulation_as_computational_reasoning_summary.R
# Base R workflow for summarizing scenario simulation, Monte Carlo uncertainty, and sensitivity.

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

trajectory_path <- file.path(tables_dir, "deterministic_simulation_trajectories.csv")
if (!file.exists(trajectory_path)) {
  stop(paste("Missing", trajectory_path, "Run the Python workflow first."))
}

trajectories <- read.csv(trajectory_path, stringsAsFactors = FALSE)
scenario_names <- unique(trajectories$scenario_name)

png(file.path(figures_dir, "deterministic_simulation_trajectories.png"), width = 1400, height = 850)
plot(NULL, xlim = range(trajectories$time_step), ylim = range(trajectories$stock), xlab = "Time step", ylab = "Stock", main = "Deterministic Simulation Trajectories")
for (scenario in scenario_names) {
  subset_data <- trajectories[trajectories$scenario_name == scenario, ]
  lines(subset_data$time_step, subset_data$stock, lwd = 2)
}
legend("topleft", legend = scenario_names, lty = 1, lwd = 2, bty = "n")
grid()
dev.off()

summary_path <- file.path(tables_dir, "deterministic_simulation_summary.csv")
summary_data <- read.csv(summary_path, stringsAsFactors = FALSE)
write.csv(summary_data, file.path(tables_dir, "r_deterministic_simulation_summary.csv"), row.names = FALSE)

mc_path <- file.path(tables_dir, "monte_carlo_simulation_runs.csv")
if (file.exists(mc_path)) {
  mc_data <- read.csv(mc_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "monte_carlo_final_stock_histogram.png"), width = 1200, height = 800)
  hist(mc_data$final_stock, breaks = 25, main = "Monte Carlo Final Stock Distribution", xlab = "Final stock", ylab = "Run count")
  grid()
  dev.off()
}

sweep_path <- file.path(tables_dir, "parameter_sweep.csv")
if (file.exists(sweep_path)) {
  sweep_data <- read.csv(sweep_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "intervention_sensitivity_sweep.png"), width = 1200, height = 800)
  plot(sweep_data$intervention_strength, sweep_data$final_stock, type = "b", lwd = 2, xlab = "Intervention strength", ylab = "Final stock", main = "Parameter Sweep: Intervention Strength vs. Final Stock")
  grid()
  dev.off()
}

checklist_path <- file.path(tables_dir, "simulation_review_checklist.csv")
if (file.exists(checklist_path)) {
  checklist_data <- read.csv(checklist_path, stringsAsFactors = FALSE)
  status_counts <- table(checklist_data$status)
  png(file.path(figures_dir, "simulation_review_checklist_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count", main = "Simulation Review Checklist Status")
  grid()
  dev.off()
}

r_summary <- data.frame(
  scenario_count = length(scenario_names),
  average_final_stock = mean(summary_data$final_stock),
  minimum_final_stock = min(summary_data$final_stock),
  maximum_final_stock = max(summary_data$final_stock)
)
write.csv(r_summary, file.path(tables_dir, "r_simulation_summary.csv"), row.names = FALSE)
print(r_summary)
