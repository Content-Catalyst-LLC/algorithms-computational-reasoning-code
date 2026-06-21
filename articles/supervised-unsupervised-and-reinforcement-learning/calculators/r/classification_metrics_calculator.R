args <- commandArgs(trailingOnly = TRUE)
values <- as.numeric(args)
if (length(values) != 4) stop("Usage: Rscript classification_metrics_calculator.R tp fp tn fn")
tp <- values[1]; fp <- values[2]; tn <- values[3]; fn <- values[4]
total <- max(1, tp + fp + tn + fn)
accuracy <- (tp + tn) / total
precision <- tp / max(1, tp + fp)
recall <- tp / max(1, tp + fn)
f1 <- ifelse(precision + recall == 0, 0, 2 * precision * recall / (precision + recall))
cat(sprintf("accuracy=%.6f\nprecision=%.6f\nrecall=%.6f\nf1=%.6f\n", accuracy, precision, recall, f1))
