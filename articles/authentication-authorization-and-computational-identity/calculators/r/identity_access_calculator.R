# identity_access_calculator.R
# Base R calculator for identity and access governance scores.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), "../.."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

out_dir <- file.path(article_root, "calculators", "outputs")
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)

weights <- c(
  authentication_strength = 0.10,
  authorization_granularity = 0.11,
  least_privilege_alignment = 0.11,
  session_token_control = 0.09,
  machine_identity_governance = 0.09,
  audit_logging = 0.10,
  access_lifecycle_review = 0.09,
  privilege_escalation_controls = 0.09,
  privacy_and_inclusion_review = 0.08,
  incident_response = 0.06,
  governance_ownership = 0.06,
  communication_clarity = 0.02
)

scenarios <- data.frame(
  scenario = c("mature_identity_governance", "legacy_overprivileged_access"),
  authentication_strength = c(0.88, 0.36),
  authorization_granularity = c(0.84, 0.24),
  least_privilege_alignment = c(0.80, 0.20),
  session_token_control = c(0.82, 0.28),
  machine_identity_governance = c(0.78, 0.18),
  audit_logging = c(0.90, 0.30),
  access_lifecycle_review = c(0.82, 0.22),
  privilege_escalation_controls = c(0.80, 0.20),
  privacy_and_inclusion_review = c(0.76, 0.30),
  incident_response = c(0.82, 0.28),
  governance_ownership = c(0.84, 0.24),
  communication_clarity = c(0.78, 0.34)
)

metric_cols <- names(weights)
scenarios$identity_access_score <- as.numeric(as.matrix(scenarios[, metric_cols]) %*% weights) * 100
risk_cols <- setdiff(metric_cols, "communication_clarity")
scenarios$identity_access_risk <- rowMeans(1 - scenarios[, risk_cols]) * 100

write.csv(
  scenarios,
  file.path(out_dir, "r_identity_access_calculator_results.csv"),
  row.names = FALSE
)

print(scenarios[, c("scenario", "identity_access_score", "identity_access_risk")])
