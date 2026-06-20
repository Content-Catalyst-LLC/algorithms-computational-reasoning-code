# Small R calculator for strategic manipulation incentives.
args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  calculator_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  calculator_root <- getwd()
}
outputs_dir <- file.path(calculator_root, "outputs")
if (!dir.exists(outputs_dir)) dir.create(outputs_dir, recursive = TRUE)
rows <- expand.grid(detection_probability = c(0, 0.25, 0.50, 0.75, 1.0), penalty = c(0, 3, 6, 9, 12))
rows$reward <- 10
rows$manipulation_cost <- 3
rows$net_gain <- rows$reward - rows$manipulation_cost - rows$detection_probability * rows$penalty
rows$manipulation_attractive <- rows$net_gain > 0
output_path <- file.path(outputs_dir, "r_strategic_behavior_calculator.csv")
write.csv(rows, output_path, row.names = FALSE)
print(output_path)
