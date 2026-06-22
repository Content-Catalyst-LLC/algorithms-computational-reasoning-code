# Monitoring Notes

A model's performance is a relationship between model and environment.

Distribution shift can appear in inputs, labels, domains, time, and feedback pathways.
Model decay can affect accuracy, calibration, fairness, safety, robustness, trust, and usefulness.
Input drift may be visible before labels are available.
Calibration drift can be dangerous even when ranking performance remains acceptable.
Retraining should not be automatic because new data may be feedback-shaped or contaminated.
Rollback and suspension are part of responsible deployment design.
