# Base R workflow for summarizing approximation error, convergence, and numerical review outputs.

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

derivative_path <- file.path(tables_dir, "derivative_approximation_audit.csv")
if (!file.exists(derivative_path)) stop(paste("Missing", derivative_path, "Run the Python workflow first."))

derivative_data <- read.csv(derivative_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "derivative_absolute_error_by_resolution.png"), width = 1300, height = 850)
plot(derivative_data$resolution, derivative_data$absolute_error, log = "xy", pch = 19,
     xlab = "Step size", ylab = "Absolute error", main = "Derivative Approximation Error by Step Size")
grid()
dev.off()

integration_path <- file.path(tables_dir, "integration_approximation_audit.csv")
if (file.exists(integration_path)) {
  integration_data <- read.csv(integration_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "integration_absolute_error_by_resolution.png"), width = 1300, height = 850)
  plot(integration_data$resolution, integration_data$absolute_error, log = "xy", pch = 19,
       xlab = "Subintervals", ylab = "Absolute error", main = "Integration Approximation Error by Resolution")
  grid()
  dev.off()
}

root_path <- file.path(tables_dir, "root_finding_audit.csv")
if (file.exists(root_path)) {
  root_data <- read.csv(root_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "root_finding_absolute_error.png"), width = 1300, height = 850)
  plot(root_data$tolerance, root_data$absolute_error, log = "xy", pch = 19,
       xlab = "Tolerance", ylab = "Absolute error", main = "Root Finding Error by Tolerance")
  grid()
  dev.off()
}

ode_path <- file.path(tables_dir, "ode_time_stepping_audit.csv")
if (file.exists(ode_path)) {
  ode_data <- read.csv(ode_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "ode_time_stepping_absolute_error.png"), width = 1300, height = 850)
  plot(ode_data$resolution, ode_data$absolute_error, log = "xy", pch = 19,
       xlab = "Step size", ylab = "Absolute error", main = "ODE Time-Stepping Error by Step Size")
  grid()
  dev.off()
}

checklist_path <- file.path(tables_dir, "numerical_approximation_checklist.csv")
if (file.exists(checklist_path)) {
  checklist_data <- read.csv(checklist_path, stringsAsFactors = FALSE)
  status_counts <- table(checklist_data$status)
  png(file.path(figures_dir, "numerical_approximation_checklist_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count", main = "Numerical Approximation Checklist Status")
  grid()
  dev.off()
}

summary_path <- file.path(tables_dir, "numerical_approximation_summary.csv")
summary_data <- read.csv(summary_path, stringsAsFactors = FALSE)

r_summary <- data.frame(
  workflow_summary_rows = nrow(summary_data),
  best_derivative_method = summary_data$best_derivative_method[1],
  best_integration_method = summary_data$best_integration_method[1],
  best_root_method = summary_data$best_root_method[1],
  best_ode_method = summary_data$best_ode_method[1],
  review_items_needing_attention = summary_data$review_items_needing_attention[1]
)

write.csv(r_summary, file.path(tables_dir, "r_numerical_approximation_summary.csv"), row.names = FALSE)
print(r_summary)
