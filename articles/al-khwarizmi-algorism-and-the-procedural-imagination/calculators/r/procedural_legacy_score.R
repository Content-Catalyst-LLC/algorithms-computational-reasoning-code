args <- commandArgs(trailingOnly = TRUE)
procedure <- ifelse(length(args) >= 1, as.numeric(args[1]), 0.94)
representation <- ifelse(length(args) >= 2, as.numeric(args[2]), 0.96)
transmission <- ifelse(length(args) >= 3, as.numeric(args[3]), 0.92)
application <- ifelse(length(args) >= 4, as.numeric(args[4]), 0.90)
modern_resonance <- ifelse(length(args) >= 5, as.numeric(args[5]), 0.94)

score <- mean(c(procedure, representation, transmission, application, modern_resonance))
cat(sprintf("procedural_legacy_score=%.6f\n", score))
