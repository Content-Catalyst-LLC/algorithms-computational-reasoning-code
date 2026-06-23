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

map_path <- file.path(tables_dir, "wiener_cybernetic_feedback_map.csv")
summary_path <- file.path(tables_dir, "wiener_cybernetic_feedback_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

wiener_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "wiener_feedback_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(wiener_map[, c("feedback_centrality", "control_relevance", "communication_relevance", "prediction_relevance", "stability_relevance", "amplification_risk", "automation_ethics", "ai_relevance", "institutional_relevance", "governance_caution")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = wiener_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Norbert Wiener, Cybernetics, and Feedback in Computation")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "wiener_cybernetic_score_by_theme.png"), width = 1000, height = 750)
barplot(wiener_map$cybernetic_score,
        names.arg = wiener_map$theme_id,
        las = 2,
        ylab = "Cybernetic Feedback Score",
        main = "Wiener Cybernetic Feedback Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_cybernetic_score = summary$mean_cybernetic_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Wiener should be studied as a theorist of feedback, control, communication, prediction, automation ethics, and governance in computational systems."
)

write.csv(r_summary, file.path(tables_dir, "r_wiener_feedback_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
