# adversarial_thinking_computational_systems_summary.R
# Base R workflow for summarizing adversarial readiness and risk.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

setwd(article_root)

tables_dir <- file.path(article_root, "outputs", "tables")
figures_dir <- file.path(article_root, "outputs", "figures")

if (!dir.exists(tables_dir)) {
  dir.create(tables_dir, recursive = TRUE)
}

if (!dir.exists(figures_dir)) {
  dir.create(figures_dir, recursive = TRUE)
}

audit_path <- file.path(tables_dir, "adversarial_readiness_audit.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

data <- read.csv(audit_path, stringsAsFactors = FALSE)

summary_table <- data.frame(
  case_count = nrow(data),
  average_adversarial_readiness_score = mean(data$adversarial_readiness_score),
  average_adversarial_risk_score = mean(data$adversarial_risk_score),
  highest_readiness_case = data$case_name[which.max(data$adversarial_readiness_score)],
  highest_risk_case = data$case_name[which.max(data$adversarial_risk_score)]
)

write.csv(
  summary_table,
  file.path(tables_dir, "r_adversarial_readiness_summary.csv"),
  row.names = FALSE
)

comparison_matrix <- rbind(
  data$adversarial_readiness_score,
  data$adversarial_risk_score
)

colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c(
  "Adversarial readiness score",
  "Adversarial risk score"
)

png(
  file.path(figures_dir, "adversarial_readiness_score_vs_risk.png"),
  width = 1500,
  height = 850
)

barplot(
  comparison_matrix,
  beside = TRUE,
  las = 2,
  ylim = c(0, 100),
  ylab = "Score",
  main = "Adversarial Readiness Score vs. Risk"
)

legend(
  "topleft",
  legend = rownames(comparison_matrix),
  pch = 15,
  bty = "n"
)

grid()
dev.off()

evasion_path <- file.path(tables_dir, "threshold_evasion_demo.csv")

if (file.exists(evasion_path)) {
  evasion_data <- read.csv(evasion_path, stringsAsFactors = FALSE)

  png(
    file.path(figures_dir, "threshold_evasion_scores.png"),
    width = 1400,
    height = 850
  )

  score_matrix <- rbind(
    evasion_data$original_score,
    evasion_data$shifted_score
  )

  colnames(score_matrix) <- evasion_data$case_id
  rownames(score_matrix) <- c("Original score", "Shifted score")

  barplot(
    score_matrix,
    beside = TRUE,
    las = 2,
    ylim = c(0, 1),
    ylab = "Score",
    main = "Threshold Evasion Demonstration"
  )

  abline(h = unique(evasion_data$threshold)[1], lty = 2)
  legend("topleft", legend = rownames(score_matrix), pch = 15, bty = "n")
  grid()
  dev.off()
}

perturbation_path <- file.path(tables_dir, "perturbation_sensitivity_demo.csv")

if (file.exists(perturbation_path)) {
  perturbation_data <- read.csv(perturbation_path, stringsAsFactors = FALSE)

  png(
    file.path(figures_dir, "perturbation_sensitivity_margins.png"),
    width = 1400,
    height = 850
  )

  plot(
    perturbation_data$base_margin,
    perturbation_data$shifted_margin,
    pch = 19,
    xlab = "Base margin",
    ylab = "Shifted margin",
    main = "Perturbation Sensitivity"
  )

  abline(h = 0, lty = 2)
  abline(v = 0, lty = 2)
  grid()
  dev.off()
}

surface_path <- file.path(tables_dir, "attack_surface_inventory.csv")

if (file.exists(surface_path)) {
  surface_data <- read.csv(surface_path, stringsAsFactors = FALSE)
  risk_counts <- table(surface_data$risk_level)

  png(
    file.path(figures_dir, "attack_surface_risk_counts.png"),
    width = 1100,
    height = 750
  )

  barplot(
    risk_counts,
    ylim = c(0, max(risk_counts) + 1),
    ylab = "Count",
    main = "Attack Surface Risk Counts"
  )

  grid()
  dev.off()
}

print(summary_table)
