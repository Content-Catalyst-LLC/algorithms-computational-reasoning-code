# algorithmic_trust_calculator.R
args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  root <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
} else {
  root <- getwd()
}

out_dir <- file.path(root, "calculators", "outputs")
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)

trust_quality <- function(verification, validation, security, provenance, monitoring, governance) {
  100 * (0.18 * verification + 0.18 * validation + 0.18 * security + 0.16 * provenance + 0.15 * monitoring + 0.15 * governance)
}

residual_risk <- function(initial_likelihood, initial_impact, control_strength) {
  100 * initial_likelihood * initial_impact * (1 - control_strength)
}

calibration_gap <- function(human_reliance, system_reliability) {
  abs(human_reliance - system_reliability)
}

result <- data.frame(
  trust_quality_score = trust_quality(0.88, 0.82, 0.88, 0.90, 0.84, 0.82),
  residual_risk_score = residual_risk(0.70, 0.75, 0.62),
  calibration_gap = calibration_gap(0.88, 0.72)
)

write.csv(result, file.path(out_dir, "algorithmic_trust_calculator_r.csv"), row.names = FALSE)
print(result)
