args <- commandArgs(trailingOnly = TRUE)
probability <- ifelse(length(args) >= 1, as.numeric(args[1]), 0.82)
benefit_if_act <- ifelse(length(args) >= 2, as.numeric(args[2]), 0.88)
cost_if_act <- ifelse(length(args) >= 3, as.numeric(args[3]), 0.30)
loss_if_miss <- ifelse(length(args) >= 4, as.numeric(args[4]), 0.92)
calibration <- ifelse(length(args) >= 5, as.numeric(args[5]), 0.78)
uncertainty_communication <- ifelse(length(args) >= 6, as.numeric(args[6]), 0.74)
human_review <- ifelse(length(args) >= 7, as.numeric(args[7]), 0.82)
contestability <- ifelse(length(args) >= 8, as.numeric(args[8]), 0.70)
governance <- ifelse(length(args) >= 9, as.numeric(args[9]), 0.76)
threshold <- ifelse(length(args) >= 10, as.numeric(args[10]), 0.70)

expected_value <- probability * benefit_if_act - cost_if_act
expected_loss <- probability * loss_if_miss
readiness <- mean(c(calibration, uncertainty_communication, human_review, contestability, governance))
threshold_action <- probability >= threshold

cat(sprintf("expected_value_of_action=%.6f\n", expected_value))
cat(sprintf("expected_loss_if_no_action=%.6f\n", expected_loss))
cat(sprintf("decision_support_readiness_score=%.6f\n", readiness))
cat(sprintf("threshold_action=%s\n", tolower(as.character(threshold_action))))
