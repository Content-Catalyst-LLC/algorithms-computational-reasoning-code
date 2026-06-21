# simulation_calculator.R
# Self-contained calculator for simple simulation reasoning checks.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  root <- getwd()
}
out <- file.path(root, "outputs")
dir.create(out, recursive = TRUE, showWarnings = FALSE)

stock <- 100
rows <- data.frame(time_step = integer(), stock = numeric())
for (t in 0:30) {
  rows <- rbind(rows, data.frame(time_step = t, stock = round(stock, 6)))
  stock <- max(0, stock + 0.08 * stock - 0.03 * stock - 0.04 * stock)
}
path <- file.path(out, "simulation_calculator_output_r.csv")
write.csv(rows, path, row.names = FALSE)
print(tail(rows, 1))
print(path)
