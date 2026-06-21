# algorithms_in_scientific_computing_summary.R
# Base R workflow for summarizing numerical approximation, convergence, and scientific computing outputs.

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

derivative_path <- file.path(tables_dir, "finite_difference_derivative_study.csv")

if (!file.exists(derivative_path)) {
  stop(paste("Missing", derivative_path, "Run the Python workflow first."))
}

derivative_data <- read.csv(derivative_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "finite_difference_derivative_error.png"), width = 1300, height = 850)
plot(
  derivative_data$step_size,
  derivative_data$absolute_error,
  log = "xy",
  pch = 19,
  xlab = "Step size",
  ylab = "Absolute error",
  main = "Finite Difference Derivative Error"
)
grid()
dev.off()

integration_path <- file.path(tables_dir, "numerical_integration_study.csv")

if (file.exists(integration_path)) {
  integration_data <- read.csv(integration_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "numerical_integration_error.png"), width = 1300, height = 850)
  plot(
    integration_data$subintervals,
    integration_data$absolute_error,
    log = "xy",
    type = "b",
    pch = 19,
    xlab = "Subintervals",
    ylab = "Absolute error",
    main = "Numerical Integration Error"
  )
  grid()
  dev.off()
}

ode_path <- file.path(tables_dir, "ode_convergence_study.csv")

if (file.exists(ode_path)) {
  ode_data <- read.csv(ode_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "ode_solver_error_by_step_size.png"), width = 1400, height = 850)
  plot(
    ode_data$step_size,
    ode_data$absolute_error,
    log = "xy",
    pch = 19,
    xlab = "Step size",
    ylab = "Absolute error",
    main = "ODE Solver Error by Step Size"
  )
  grid()
  dev.off()
}

mc_path <- file.path(tables_dir, "monte_carlo_pi_summary.csv")

if (file.exists(mc_path)) {
  mc_summary <- read.csv(mc_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "monte_carlo_pi_error_by_samples.png"), width = 1300, height = 850)
  plot(
    mc_summary$samples,
    mc_summary$mean_absolute_error,
    log = "xy",
    type = "b",
    pch = 19,
    xlab = "Samples",
    ylab = "Mean absolute error",
    main = "Monte Carlo Error by Sample Size"
  )
  grid()
  dev.off()
}

checklist_path <- file.path(tables_dir, "scientific_computing_workflow_checklist.csv")

if (file.exists(checklist_path)) {
  checklist_data <- read.csv(checklist_path, stringsAsFactors = FALSE)
  status_counts <- table(checklist_data$status)
  png(file.path(figures_dir, "scientific_computing_checklist_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count", main = "Scientific Computing Workflow Checklist Status")
  grid()
  dev.off()
}

summary_path <- file.path(tables_dir, "scientific_computing_audit_summary.csv")
summary_data <- read.csv(summary_path, stringsAsFactors = FALSE)

r_summary <- data.frame(
  workflow_summary_rows = nrow(summary_data),
  best_ode_method = summary_data$best_ode_method[1],
  best_derivative_method = summary_data$best_derivative_method[1],
  review_items_needing_attention = summary_data$review_items_needing_attention[1]
)

write.csv(r_summary, file.path(tables_dir, "r_scientific_computing_summary.csv"), row.names = FALSE)
print(r_summary)
