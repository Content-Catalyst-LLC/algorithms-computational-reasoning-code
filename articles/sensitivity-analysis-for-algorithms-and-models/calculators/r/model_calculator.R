# Self-contained sensitivity-analysis calculator in base R.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
} else {
  root <- normalizePath(file.path(getwd(), "calculators"), mustWork = FALSE)
}

out_dir <- file.path(root, "outputs")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

model <- function(x, demand, capacity, failure, adaptation) {
  max(0, min(1, 0.5 + 0.30 * demand + 0.25 * failure - 0.20 * capacity - 0.15 * adaptation + 0.05 * x))
}

finite_difference <- function(parameter, baseline, h = 0.01) {
  plus <- baseline
  plus[[parameter]] <- plus[[parameter]] + h
  y0 <- do.call(model, baseline)
  y1 <- do.call(model, plus)
  sensitivity <- (y1 - y0) / h
  normalized <- ifelse(y0 != 0 && baseline[[parameter]] != 0, ((y1 - y0) / y0) / (h / baseline[[parameter]]), 0)
  data.frame(
    parameter = parameter,
    baseline_output = round(y0, 6),
    perturbed_output = round(y1, 6),
    local_sensitivity = round(sensitivity, 6),
    normalized_sensitivity = round(normalized, 6)
  )
}

baseline <- list(x = 1.0, demand = 0.45, capacity = 0.35, failure = 0.25, adaptation = 0.30)
rows <- do.call(rbind, lapply(c("demand", "capacity", "failure", "adaptation"), finite_difference, baseline = baseline))
path <- file.path(out_dir, "r_sensitivity_calculator.csv")
write.csv(rows, path, row.names = FALSE)
print(path)
