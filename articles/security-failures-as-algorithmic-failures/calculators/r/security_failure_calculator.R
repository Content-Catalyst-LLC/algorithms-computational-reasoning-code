# security_failure_calculator.R
# Base R calculator for failure-resistance and algorithmic failure risk.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

output_dir <- file.path(article_root, "calculators", "outputs")
if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE)
}

weights <- c(
  assumption_quality = 0.08,
  threat_model_coverage = 0.10,
  input_boundary_control = 0.10,
  authorization_control = 0.10,
  cryptographic_procedure = 0.08,
  dependency_governance = 0.08,
  configuration_safety = 0.08,
  state_timing_control = 0.08,
  logging_traceability = 0.08,
  monitoring_detection = 0.08,
  incident_response = 0.06,
  lifecycle_review = 0.05,
  governance_ownership = 0.03
)

scenario <- c(
  assumption_quality = 0.62,
  threat_model_coverage = 0.58,
  input_boundary_control = 0.70,
  authorization_control = 0.55,
  cryptographic_procedure = 0.66,
  dependency_governance = 0.50,
  configuration_safety = 0.54,
  state_timing_control = 0.48,
  logging_traceability = 0.60,
  monitoring_detection = 0.52,
  incident_response = 0.50,
  lifecycle_review = 0.44,
  governance_ownership = 0.46
)

score <- 100 * sum(weights * scenario[names(weights)])
risk <- 100 * mean(1 - scenario[names(weights)])
control_gap <- (1 - scenario["authorization_control"]) * 0.90 * 100

result <- data.frame(
  failure_resistance_score = round(score, 3),
  algorithmic_failure_risk = round(risk, 3),
  authorization_control_gap_score = round(control_gap, 3),
  interpretation = "Higher failure resistance and lower residual risk indicate stronger algorithmic security reasoning."
)

write.csv(result, file.path(output_dir, "r_security_failure_calculator_result.csv"), row.names = FALSE)
print(result)
