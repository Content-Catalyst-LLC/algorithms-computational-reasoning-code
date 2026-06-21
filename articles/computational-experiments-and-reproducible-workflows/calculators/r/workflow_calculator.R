reproducibility_score <- function(has_code = TRUE,
                                  has_data = TRUE,
                                  has_parameters = TRUE,
                                  has_seed = TRUE,
                                  has_environment = TRUE,
                                  has_manifest = TRUE,
                                  has_validation = FALSE) {
  checks <- c(
    code = has_code,
    data = has_data,
    parameters = has_parameters,
    seed = has_seed,
    environment = has_environment,
    manifest = has_manifest,
    validation = has_validation
  )
  score <- sum(checks) / length(checks)
  data.frame(score = round(score, 4), percentage = round(100 * score, 2))
}

sample_error <- function(std_dev = 10, samples = 1000) {
  se <- std_dev / sqrt(samples)
  data.frame(std_dev = std_dev, samples = samples, standard_error = round(se, 8), approx_95_margin = round(1.96 * se, 8))
}

print(reproducibility_score())
print(sample_error())
