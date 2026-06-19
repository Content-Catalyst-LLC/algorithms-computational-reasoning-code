data <- read.csv("data/synthetic_edge_embedded_cases.csv", stringsAsFactors = FALSE)
data$edge_embedded_score <- 100 * (0.11*data$latency_discipline + 0.09*data$power_awareness + 0.08*data$memory_awareness + 0.10*data$sensor_validation + 0.09*data$offline_behavior + 0.08*data$update_safety + 0.10*data$security_design + 0.10*data$observability + 0.11*data$fail_safe_design + 0.06*data$data_minimization + 0.05*data$governance_review + 0.03*data$communication_clarity)
data$edge_embedded_risk <- 100 * rowMeans(1 - data[, c("latency_discipline","power_awareness","sensor_validation","offline_behavior","update_safety","security_design","observability","fail_safe_design","governance_review")])
dir.create("outputs/tables", recursive=TRUE, showWarnings=FALSE)
dir.create("outputs/figures", recursive=TRUE, showWarnings=FALSE)
write.csv(data, "outputs/tables/r_edge_embedded_summary.csv", row.names=FALSE)
png("outputs/figures/r_edge_embedded_score_vs_risk.png", width=1500, height=850)
m <- rbind(data$edge_embedded_score, data$edge_embedded_risk)
colnames(m) <- data$case_name
rownames(m) <- c("Edge embedded score", "Edge embedded risk")
barplot(m, beside=TRUE, las=2, ylim=c(0,100), ylab="Score", main="Edge and Embedded Algorithm Score vs. Risk")
legend("topleft", legend=rownames(m), pch=15, bty="n"); grid(); dev.off()
timing <- read.csv("data/synthetic_edge_timing_power.csv", stringsAsFactors=FALSE)
timing$edge_response_time_ms <- timing$sense_ms + timing$filter_ms + timing$compute_ms + timing$actuate_ms
timing$cloud_response_time_ms <- timing$sense_ms + timing$uplink_ms + timing$cloud_compute_ms + timing$downlink_ms + timing$actuate_ms
timing$edge_meets_deadline <- timing$edge_response_time_ms <= timing$deadline_ms
timing$cloud_meets_deadline <- timing$cloud_response_time_ms <= timing$deadline_ms
timing$battery_life_hours <- timing$battery_wh / timing$average_power_w
timing$local_action <- ifelse(timing$signal_value >= timing$threshold, "alert", "monitor")
write.csv(timing, "outputs/tables/r_edge_timing_power_summary.csv", row.names=FALSE)
print(data)
