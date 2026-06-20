# adversarial_risk_calculator.R
# Educational calculator for adversarial readiness and residual risk.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

out_dir <- file.path(article_root, "calculators", "outputs")
if (!dir.exists(out_dir)) {
  dir.create(out_dir, recursive = TRUE)
}

clamp <- function(value, low = 0, high = 100) {
  max(low, min(high, value))
}

readiness_score <- function(threat_model, attack_surface, monitoring, defense_depth, incident_response, governance) {
  clamp(100 * (
    0.18 * threat_model +
      0.18 * attack_surface +
      0.18 * monitoring +
      0.18 * defense_depth +
      0.14 * incident_response +
      0.14 * governance
  ))
}

attack_success_probability <- function(capability, exposure, control_strength) {
  clamp(100 * capability * exposure * (1 - control_strength))
}

residual_risk <- function(initial_risk, mitigation_effectiveness) {
  clamp(initial_risk * (1 - mitigation_effectiveness))
}

results <- data.frame(
  scenario = c("strong_defense", "partial_defense", "weak_defense"),
  readiness = c(
    readiness_score(0.86, 0.82, 0.88, 0.82, 0.80, 0.78),
    readiness_score(0.62, 0.58, 0.54, 0.50, 0.46, 0.48),
    readiness_score(0.28, 0.34, 0.24, 0.20, 0.18, 0.22)
  ),
  attack_success_probability = c(
    attack_success_probability(0.72, 0.62, 0.82),
    attack_success_probability(0.76, 0.70, 0.44),
    attack_success_probability(0.86, 0.78, 0.18)
  ),
  residual_risk = c(
    residual_risk(78, 0.64),
    residual_risk(82, 0.38),
    residual_risk(90, 0.16)
  )
)

write.csv(results, file.path(out_dir, "r_adversarial_risk_calculator_results.csv"), row.names = FALSE)
print(results)
