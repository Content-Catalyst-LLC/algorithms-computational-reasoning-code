# cryptographic_algorithms_secure_communication_summary.R
# Base R workflow for summarizing cryptographic governance and secure-communication audits.

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

audit_path <- file.path(tables_dir, "secure_communication_governance_audit.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

data <- read.csv(audit_path, stringsAsFactors = FALSE)

summary_table <- data.frame(
  case_count = nrow(data),
  average_secure_communication_score = mean(data$secure_communication_score),
  average_secure_communication_risk = mean(data$secure_communication_risk),
  highest_score_case = data$case_name[which.max(data$secure_communication_score)],
  highest_risk_case = data$case_name[which.max(data$secure_communication_risk)]
)

write.csv(
  summary_table,
  file.path(tables_dir, "r_secure_communication_governance_summary.csv"),
  row.names = FALSE
)

comparison_matrix <- rbind(
  data$secure_communication_score,
  data$secure_communication_risk
)

colnames(comparison_matrix) <- data$case_name
rownames(comparison_matrix) <- c(
  "Secure communication score",
  "Secure communication risk"
)

png(
  file.path(figures_dir, "secure_communication_score_vs_risk.png"),
  width = 1500,
  height = 850
)

barplot(
  comparison_matrix,
  beside = TRUE,
  las = 2,
  ylim = c(0, 100),
  ylab = "Score",
  main = "Secure Communication Governance Score vs. Risk"
)

legend(
  "topleft",
  legend = rownames(comparison_matrix),
  pch = 15,
  bty = "n"
)

grid()
dev.off()

auth_path <- file.path(tables_dir, "message_authentication_demo.csv")

if (file.exists(auth_path)) {
  auth_data <- read.csv(auth_path, stringsAsFactors = FALSE)

  write.csv(
    auth_data,
    file.path(tables_dir, "r_message_authentication_demo.csv"),
    row.names = FALSE
  )

  auth_counts <- table(auth_data$verified)

  png(
    file.path(figures_dir, "message_authentication_verification_counts.png"),
    width = 1200,
    height = 800
  )

  barplot(
    auth_counts,
    ylim = c(0, max(auth_counts) + 1),
    ylab = "Count",
    main = "Message Authentication Verification Outcomes"
  )

  grid()
  dev.off()
}

inventory_path <- file.path(tables_dir, "approved_primitive_inventory.csv")

if (file.exists(inventory_path)) {
  inventory_data <- read.csv(inventory_path, stringsAsFactors = FALSE)

  write.csv(
    inventory_data,
    file.path(tables_dir, "r_approved_primitive_inventory.csv"),
    row.names = FALSE
  )
}

print(summary_table)
