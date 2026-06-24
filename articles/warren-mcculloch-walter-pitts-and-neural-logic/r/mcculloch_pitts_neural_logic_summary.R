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

map_path <- file.path(tables_dir, "mcculloch_pitts_neural_logic_map.csv")
summary_path <- file.path(tables_dir, "neural_logic_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

logic_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "neural_logic_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(logic_map[, c("logical_clarity", "neural_abstraction", "computational_relevance", "cybernetic_connection", "ai_lineage", "biological_caution", "historical_influence", "interpretability", "formal_tractability", "responsible_use_relevance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = logic_map$concept_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Warren McCulloch, Walter Pitts, and Neural Logic")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "neural_logic_score_by_concept.png"), width = 1000, height = 750)
barplot(logic_map$neural_logic_score,
        names.arg = logic_map$concept_id,
        las = 2,
        ylab = "Neural Logic Score",
        main = "Neural Logic Score by Concept")
grid()
dev.off()

r_summary <- data.frame(
  concepts_reviewed = summary$concepts_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_neural_logic_score = summary$mean_neural_logic_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "McCulloch-Pitts neural logic should be studied as a bridge among threshold units, symbolic logic, neural abstraction, cybernetics, automata, AI history, and responsible model interpretation."
)

write.csv(r_summary, file.path(tables_dir, "r_neural_logic_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
