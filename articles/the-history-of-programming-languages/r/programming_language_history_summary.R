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

map_path <- file.path(tables_dir, "programming_language_history_map.csv")
summary_path <- file.path(tables_dir, "programming_language_history_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

language_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "programming_language_history_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(language_map[, c("abstraction", "performance_orientation", "readability", "formal_specification", "ecosystem_depth", "domain_fit", "safety_orientation", "institutional_adoption", "historical_influence", "governance_caution")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = language_map$tradition_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "The History of Programming Languages")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "programming_language_history_score_by_tradition.png"), width = 1000, height = 750)
barplot(language_map$history_score,
        names.arg = language_map$tradition_id,
        las = 2,
        ylab = "Programming-Language History Score",
        main = "Language-History Score by Tradition")
grid()
dev.off()

r_summary <- data.frame(
  traditions_reviewed = summary$traditions_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_history_score = summary$mean_history_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Programming-language history should be studied as a layered history of expression, execution, abstraction, ecosystems, institutions, safety, and governance."
)

write.csv(r_summary, file.path(tables_dir, "r_programming_language_history_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
