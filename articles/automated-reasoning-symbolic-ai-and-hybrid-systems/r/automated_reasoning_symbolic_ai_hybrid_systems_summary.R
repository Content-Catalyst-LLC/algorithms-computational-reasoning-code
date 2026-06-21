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

summary_path <- file.path(tables_dir, "symbolic_audit_summary.csv")
constraints_path <- file.path(tables_dir, "symbolic_constraint_review.csv")
trace_path <- file.path(tables_dir, "symbolic_inference_trace.csv")

if (!file.exists(summary_path)) {
  stop(paste("Missing", summary_path, "Run the Python workflow first."))
}

summary <- read.csv(summary_path, stringsAsFactors = FALSE)
constraints <- read.csv(constraints_path, stringsAsFactors = FALSE)
trace <- read.csv(trace_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "symbolic_constraint_satisfaction.png"), width = 1100, height = 800)
barplot(constraints$satisfied,
        names.arg = constraints$constraint,
        las = 2,
        ylim = c(0, 1),
        ylab = "Satisfied",
        main = "Symbolic Constraint Review")
grid()
dev.off()

png(file.path(figures_dir, "symbolic_inference_trace_steps.png"), width = 1000, height = 750)
barplot(rep(1, nrow(trace)),
        names.arg = trace$rule_id,
        ylab = "Derived conclusion",
        main = "Symbolic Inference Trace Steps")
grid()
dev.off()

r_summary <- data.frame(
  rule_count = summary$rule_count[1],
  derived_fact_count = summary$derived_fact_count[1],
  trace_steps = summary$trace_steps[1],
  constraints_satisfied = summary$constraints_satisfied[1],
  conflicts_detected = summary$conflicts_detected[1],
  hybrid_interface_items = summary$hybrid_interface_items[1],
  diagnostic_note = "Symbolic reasoning should be reviewed through rule provenance, traceability, contradiction checks, hybrid-interface review, and use boundaries."
)

write.csv(r_summary, file.path(tables_dir, "r_symbolic_reasoning_summary.csv"), row.names = FALSE)
print(r_summary)
