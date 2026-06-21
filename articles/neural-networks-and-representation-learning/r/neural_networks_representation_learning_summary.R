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

summary_path <- file.path(tables_dir, "model_evaluation_summary.csv")
predictions_path <- file.path(tables_dir, "representation_predictions.csv")
history_path <- file.path(tables_dir, "training_history.csv")
context_path <- file.path(tables_dir, "context_performance_diagnostics.csv")

if (!file.exists(summary_path)) {
  stop(paste("Missing", summary_path, "Run the Python workflow first."))
}

evaluation <- read.csv(summary_path, stringsAsFactors = FALSE)
predictions <- read.csv(predictions_path, stringsAsFactors = FALSE)
history <- read.csv(history_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "representation_train_test_loss.png"), width = 1100, height = 800)
barplot(evaluation$mean_loss,
        names.arg = evaluation$split,
        ylab = "Mean loss",
        main = "Train/Test Representation Loss")
grid()
dev.off()

png(file.path(figures_dir, "representation_score_by_label.png"), width = 1100, height = 800)
boxplot(representation_score ~ label,
        data = subset(predictions, split == "test"),
        xlab = "Observed label",
        ylab = "Representation score",
        main = "Test Representation Scores by Label")
grid()
dev.off()

png(file.path(figures_dir, "representation_training_history.png"), width = 1200, height = 850)
plot(history$epoch,
     history$training_loss,
     type = "l",
     xlab = "Epoch",
     ylab = "Training loss",
     main = "Representation Training History")
grid()
dev.off()

if (file.exists(context_path)) {
  context_metrics <- read.csv(context_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "representation_context_accuracy.png"), width = 1100, height = 800)
  barplot(context_metrics$accuracy,
          names.arg = context_metrics$context,
          ylab = "Accuracy",
          ylim = c(0, 1),
          main = "Representation Accuracy by Context")
  grid()
  dev.off()
}

r_summary <- data.frame(
  train_accuracy = evaluation$accuracy[evaluation$split == "train"],
  test_accuracy = evaluation$accuracy[evaluation$split == "test"],
  train_loss = evaluation$mean_loss[evaluation$split == "train"],
  test_loss = evaluation$mean_loss[evaluation$split == "test"],
  diagnostic_note = "Representation performance should be reviewed with generalization, validity, subgroup behavior, and use boundaries."
)

write.csv(r_summary, file.path(tables_dir, "r_representation_learning_summary.csv"), row.names = FALSE)
print(r_summary)
