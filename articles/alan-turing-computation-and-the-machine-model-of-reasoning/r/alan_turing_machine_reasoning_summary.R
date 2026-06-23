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

map_path <- file.path(tables_dir, "turing_machine_reasoning_map.csv")
summary_path <- file.path(tables_dir, "turing_reasoning_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

turing_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "turing_reasoning_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(turing_map[, c("formalization", "machine_abstraction", "symbolic_representation", "universality", "decidability", "limit_awareness", "reasoning_relevance", "ai_relevance", "governance_caution", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = turing_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Alan Turing, Computation, and the Machine Model of Reasoning")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "turing_reasoning_score_by_theme.png"), width = 1000, height = 750)
barplot(turing_map$reasoning_score,
        names.arg = turing_map$theme_id,
        las = 2,
        ylab = "Reasoning Score",
        main = "Turing Machine Reasoning Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_reasoning_score = summary$mean_reasoning_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Turing should be studied as a bridge between effective procedure, machine abstraction, universal computation, formal limits, and AI-era caution."
)

write.csv(r_summary, file.path(tables_dir, "r_turing_reasoning_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
