args <- commandArgs(trailingOnly = TRUE)
values <- as.numeric(args)
if (length(values) != 4) stop("Usage: Rscript threshold_confusion_calculator.R tp fp tn fn")
tp <- values[1]; fp <- values[2]; tn <- values[3]; fn <- values[4]
total <- max(1, tp + fp + tn + fn)
accuracy <- (tp + tn) / total
precision <- tp / max(1, tp + fp)
recall <- tp / max(1, tp + fn)
cat(sprintf("accuracy=%.6f\n", accuracy))
cat(sprintf("precision=%.6f\n", precision))
cat(sprintf("recall=%.6f\n", recall))
