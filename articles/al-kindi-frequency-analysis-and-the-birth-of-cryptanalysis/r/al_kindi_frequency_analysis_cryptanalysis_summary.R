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

map_path <- file.path(tables_dir, "cryptanalysis_map.csv")
freq_path <- file.path(tables_dir, "sample_frequency_table.csv")
summary_path <- file.path(tables_dir, "cryptanalysis_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

cryptanalysis_map <- read.csv(map_path, stringsAsFactors = FALSE)
frequency_table <- read.csv(freq_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "cryptanalysis_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(cryptanalysis_map[, c("linguistic_evidence", "counting_procedure", "inferential_structure", "cryptanalytic_relevance", "historical_significance", "ethical_caution", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = cryptanalysis_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Al-Kindī, Frequency Analysis, and Cryptanalysis Dimensions")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "sample_symbol_frequency.png"), width = 1000, height = 750)
barplot(frequency_table$relative_frequency,
        names.arg = frequency_table$symbol,
        ylab = "Relative Frequency",
        main = "Sample Cipher Symbol Frequencies")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_cryptanalysis_score = summary$mean_cryptanalysis_score[1],
  sample_symbols_reviewed = summary$sample_symbols_reviewed[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Al-Kindī’s frequency-analysis method should be studied as early algorithmic inference over language: count, rank, compare, hypothesize, test, revise, and interpret."
)

write.csv(r_summary, file.path(tables_dir, "r_cryptanalysis_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
