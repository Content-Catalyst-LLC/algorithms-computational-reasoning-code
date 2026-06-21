% Minimal Prolog facts for uncertainty quantification review.
uncertainty_source(demand, forecast_input).
uncertainty_source(capacity, planning_assumption).
uncertainty_source(failure_rate, estimated_parameter).
uncertainty_source(adaptation_rate, behavioral_parameter).
uncertainty_source(measurement_noise, measurement_error).

decision_relevant(threshold_exceedance_probability).
review_needed(structural_uncertainty).
