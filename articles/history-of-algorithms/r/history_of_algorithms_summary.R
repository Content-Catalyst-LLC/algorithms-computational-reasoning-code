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

map_path <- file.path(tables_dir, "algorithm_history_map.csv")
summary_path <- file.path(tables_dir, "algorithm_history_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

history_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "algorithm_history_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(history_map[, c("procedural_explicitness", "representation", "proof_correctness", "portability", "mechanization", "formalization", "programmability", "institutional_adoption", "governance_relevance", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = history_map$layer_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "The History of Algorithms: From Procedure to Computation")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "algorithm_history_score_by_layer.png"), width = 1000, height = 750)
barplot(history_map$history_score,
        names.arg = history_map$layer_id,
        las = 2,
        ylab = "History Score",
        main = "Algorithm History Score by Layer")
grid()
dev.off()

r_summary <- data.frame(
  layers_reviewed = summary$layers_reviewed[1],
  core_layers = summary$core_layers[1],
  major_layers = summary$major_layers[1],
  supporting_layers = summary$supporting_layers[1],
  mean_history_score = summary$mean_history_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Algorithm history is a layered movement from procedure to computation: examples, rules, notation, proof, tables, machines, programs, analysis, platforms, and governance."
)

write.csv(r_summary, file.path(tables_dir, "r_algorithm_history_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
