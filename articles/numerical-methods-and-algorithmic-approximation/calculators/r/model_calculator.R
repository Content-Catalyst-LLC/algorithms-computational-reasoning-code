f <- function(x) sin(x) + 0.25 * x * x

finite_difference <- function(x = 1, h = 0.01, method = "central") {
  if (method == "forward") return((f(x + h) - f(x)) / h)
  if (method == "central") return((f(x + h) - f(x - h)) / (2 * h))
  stop("method must be forward or central")
}

trapezoid <- function(a = 0, b = pi, n = 100) {
  h <- (b - a) / n
  xs <- seq(a, b, length.out = n + 1)
  vals <- f(xs)
  h * (0.5 * vals[1] + sum(vals[2:n]) + 0.5 * vals[n + 1])
}

bisection_root <- function(a = 1, b = 2, tol = 1e-8) {
  g <- function(x) x * x - 2
  fa <- g(a)
  fb <- g(b)
  if (fa * fb > 0) stop("Root is not bracketed")
  while (0.5 * abs(b - a) > tol) {
    m <- 0.5 * (a + b)
    fm <- g(m)
    if (fa * fm <= 0) {
      b <- m
      fb <- fm
    } else {
      a <- m
      fa <- fm
    }
  }
  0.5 * (a + b)
}

results <- data.frame(
  calculator = c("finite_difference_central", "finite_difference_forward", "trapezoid_0_pi", "bisection_sqrt2"),
  value = c(finite_difference(), finite_difference(method = "forward"), trapezoid(), bisection_root())
)

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
} else {
  script_path <- normalizePath("calculators/r/model_calculator.R", mustWork = FALSE)
}
out_dir <- file.path(dirname(dirname(script_path)), "outputs")
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
write.csv(results, file.path(out_dir, "r_calculator_results.csv"), row.names = FALSE)
print(results)
