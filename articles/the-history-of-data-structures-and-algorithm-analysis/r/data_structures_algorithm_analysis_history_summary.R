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

map_path <- file.path(tables_dir, "data_structure_algorithm_analysis_history_map.csv")
summary_path <- file.path(tables_dir, "data_structure_algorithm_analysis_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

structure_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "data_structure_algorithm_analysis_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(structure_map[, c("representation_centrality", "operation_clarity", "memory_awareness", "time_analysis", "space_analysis", "scale_sensitivity", "abstraction_maturity", "systems_relevance", "historical_influence", "governance_caution")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = structure_map$tradition_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "The History of Data Structures and Algorithm Analysis")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "data_structure_algorithm_analysis_score_by_tradition.png"), width = 1000, height = 750)
barplot(structure_map$history_score,
        names.arg = structure_map$tradition_id,
        las = 2,
        ylab = "Data-Structure and Analysis History Score",
        main = "History Score by Tradition")
grid()
dev.off()

if (file.exists(file.path(tables_dir, "growth_rate_examples.csv"))) {
  growth <- read.csv(file.path(tables_dir, "growth_rate_examples.csv"))
  png(file.path(figures_dir, "growth_rate_examples.png"), width = 950, height = 700)
  plot(growth$n, growth$linear,
       type = "b",
       log = "xy",
       xlab = "n",
       ylab = "cost",
       main = "Growth-Rate Examples")
  lines(growth$n, growth$n_log2_n, type = "b")
  lines(growth$n, growth$quadratic, type = "b")
  legend("topleft", legend = c("n", "n log2 n", "n^2"), bty = "n")
  grid()
  dev.off()
}

r_summary <- data.frame(
  traditions_reviewed = summary$traditions_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_history_score = summary$mean_history_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Data-structure and algorithm-analysis history should be studied as a joined history of representation, operation cost, memory, scale, abstraction, systems infrastructure, and governance."
)

write.csv(r_summary, file.path(tables_dir, "r_data_structure_algorithm_analysis_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
