args <- commandArgs(trailingOnly = TRUE)
procedural <- ifelse(length(args) >= 1, as.numeric(args[1]), 0.92)
transmission <- ifelse(length(args) >= 2, as.numeric(args[2]), 0.96)
practical <- ifelse(length(args) >= 3, as.numeric(args[3]), 0.88)
representation <- ifelse(length(args) >= 4, as.numeric(args[4]), 0.94)
modern <- ifelse(length(args) >= 5, as.numeric(args[5]), 0.96)

score <- mean(c(procedural, transmission, practical, representation, modern))
cat(sprintf("historical_significance_score=%.6f\n", score))
