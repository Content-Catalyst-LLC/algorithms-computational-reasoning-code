# authentication_authorization_identity_summary.R
# Base R workflow for summarizing identity and access governance audits.

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

audit_path <- file.path(tables_dir, "identity_access_governance_audit.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

data <- read.csv(audit_path, stringsAsFactors = FALSE)

summary_table <- data.frame(
  case_count = nrow(data),
  average_identity_access_score = mean(data$identity_access_score),
  average_identity_access_risk = mean(data$identity_access_risk),
  highest_score_case = data$case_name[which.max(data$identity_access_score)],
  highest_risk_case = data$case_name[which.max(data$identity_access_risk)]
)

write.csv(
  summary_table,
  file.path(tables_dir, "r_identity_access_governance_summary.csv"),
  row.names = FALSE
)

comparison_matrix <- rbind(
  data$identity_access_score,
  data$identity_access_risk
)

colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c(
  "Identity access score",
  "Identity access risk"
)

png(
  file.path(figures_dir, "identity_access_score_vs_risk.png"),
  width = 1500,
  height = 850
)

barplot(
  comparison_matrix,
  beside = TRUE,
  las = 2,
  ylim = c(0, 100),
  ylab = "Score",
  main = "Identity and Access Governance Score vs. Risk"
)

legend(
  "topleft",
  legend = rownames(comparison_matrix),
  pch = 15,
  bty = "n"
)

grid()
dev.off()

auth_path <- file.path(tables_dir, "authorization_policy_demo.csv")

if (file.exists(auth_path)) {
  auth_data <- read.csv(auth_path, stringsAsFactors = FALSE)
  decision_counts <- table(auth_data$decision)

  png(
    file.path(figures_dir, "authorization_decision_counts.png"),
    width = 1100,
    height = 750
  )

  barplot(
    decision_counts,
    ylim = c(0, max(decision_counts) + 1),
    ylab = "Count",
    main = "Authorization Policy Decisions"
  )

  grid()
  dev.off()
}

risk_path <- file.path(tables_dir, "access_risk_register.csv")

if (file.exists(risk_path)) {
  risk_data <- read.csv(risk_path, stringsAsFactors = FALSE)

  risk_matrix <- rbind(
    risk_data$inherent_access_risk,
    risk_data$residual_access_risk
  )

  colnames(risk_matrix) <- risk_data$access_path
  rownames(risk_matrix) <- c("Inherent risk", "Residual risk")

  png(
    file.path(figures_dir, "inherent_vs_residual_access_risk.png"),
    width = 1500,
    height = 850
  )

  barplot(
    risk_matrix,
    beside = TRUE,
    las = 2,
    ylim = c(0, max(risk_matrix) + 10),
    ylab = "Risk score",
    main = "Inherent vs. Residual Access Risk"
  )

  legend("topleft", legend = rownames(risk_matrix), pch = 15, bty = "n")
  grid()
  dev.off()
}

lifecycle_path <- file.path(tables_dir, "access_lifecycle_review.csv")

if (file.exists(lifecycle_path)) {
  lifecycle_data <- read.csv(lifecycle_path, stringsAsFactors = FALSE)

  png(
    file.path(figures_dir, "access_lifecycle_review_age.png"),
    width = 1400,
    height = 850
  )

  barplot(
    lifecycle_data$last_review_days,
    names.arg = lifecycle_data$identity,
    las = 2,
    ylab = "Days since last review",
    main = "Access Lifecycle Review Age"
  )

  abline(h = 90, lty = 2)
  grid()
  dev.off()
}

password_path <- file.path(tables_dir, "password_storage_demo.csv")

if (file.exists(password_path)) {
  password_data <- read.csv(password_path, stringsAsFactors = FALSE)
  write.csv(password_data, file.path(tables_dir, "r_password_storage_demo.csv"), row.names = FALSE)
}

print(summary_table)
