objective <- function(x) {
  (x - 2)^2 + 1
}

xs <- seq(-3, 5, by = 1)
rows <- data.frame(
  x = xs,
  objective = objective(xs),
  is_global_minimum = xs == 2
)

script_args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", script_args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

out_dir <- file.path(article_root, "calculators", "outputs")
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
write.csv(rows, file.path(out_dir, "convex_quadratic_calculator.csv"), row.names = FALSE)
print(rows[which.min(rows$objective), ])
