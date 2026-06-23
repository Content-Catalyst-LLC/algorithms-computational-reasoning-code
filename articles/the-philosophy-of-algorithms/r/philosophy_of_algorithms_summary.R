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
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

map_path <- file.path(tables_dir, "algorithmic_philosophy_review_map.csv")
summary_path <- file.path(tables_dir, "algorithmic_philosophy_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

review_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "algorithmic_philosophy_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(review_map[, c("formalization_intensity", "abstraction_risk", "representation_risk", "delegation_level", "opacity", "optimization_pressure", "contestability_need", "institutional_consequence", "human_judgment_requirement", "governance_urgency")]))
barplot(score_matrix, beside = TRUE, names.arg = review_map$domain_id, las = 2, ylim = c(0, 1), ylab = "Interpretive Score", main = "The Philosophy of Algorithms")
legend("bottomright", legend = rownames(score_matrix), cex = 0.68, bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "algorithmic_philosophy_review_score_by_domain.png"), width = 1000, height = 750)
barplot(review_map$review_score, names.arg = review_map$domain_id, las = 2, ylab = "Philosophical Review Score", main = "Algorithmic Philosophy Review Score by Domain")
grid()
dev.off()

if (file.exists(file.path(tables_dir, "delegation_risk_examples.csv"))) {
  delegation <- read.csv(file.path(tables_dir, "delegation_risk_examples.csv"))
  png(file.path(figures_dir, "delegation_risk_examples.png"), width = 950, height = 700)
  barplot(delegation$delegation_risk, names.arg = delegation$case_id, las = 2, ylim = c(0, 1), ylab = "Delegation Risk", main = "Delegation Risk Examples")
  grid()
  dev.off()
}

r_summary <- data.frame(
  domains_reviewed = summary$domains_reviewed[1],
  high_priority_reviews = summary$high_priority_reviews[1],
  review_needed = summary$review_needed[1],
  routine_reviews = summary$routine_reviews[1],
  mean_review_score = summary$mean_review_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "The philosophy of algorithms examines procedure, formalization, abstraction, representation, delegation, explanation, limits, institutions, and responsibility."
)

write.csv(r_summary, file.path(tables_dir, "r_algorithmic_philosophy_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
