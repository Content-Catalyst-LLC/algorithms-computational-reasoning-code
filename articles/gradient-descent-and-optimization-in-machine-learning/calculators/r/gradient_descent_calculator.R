# Base R gradient descent calculator.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

outputs_dir <- file.path(article_root, "calculators", "outputs")
dir.create(outputs_dir, recursive = TRUE, showWarnings = FALSE)

data <- data.frame(
  x = c(-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0),
  y = c(-2.85, -1.77, -0.67, 0.32, 1.47, 2.64, 3.63, 4.87, 5.82)
)

mse <- function(weight, bias) {
  mean((data$y - (weight * data$x + bias))^2)
}

train <- function(rate = 0.08, steps = 80) {
  weight <- 0
  bias <- 0
  rows <- data.frame()

  for (i in 0:steps) {
    rows <- rbind(rows, data.frame(
      step = i,
      learning_rate = rate,
      weight = weight,
      bias = bias,
      loss = mse(weight, bias)
    ))

    if (i < steps) {
      prediction <- weight * data$x + bias
      error <- prediction - data$y
      grad_w <- mean(2 * error * data$x)
      grad_b <- mean(2 * error)
      weight <- weight - rate * grad_w
      bias <- bias - rate * grad_b
    }
  }

  rows
}

trace <- train()
write.csv(trace, file.path(outputs_dir, "r_gradient_descent_calculator_trace.csv"), row.names = FALSE)
print(tail(trace, 1))
