% Conceptual Prolog facts for gradient descent governance.

optimizer(gradient_descent).
optimizer(stochastic_gradient_descent).
optimizer(mini_batch_gradient_descent).
optimizer(momentum).
optimizer(adam).

requires_review(loss_function).
requires_review(learning_rate).
requires_review(training_data).
requires_review(validation_split).
requires_review(fairness_metrics).
requires_review(reproducibility).

risk(overfitting) :- weak(validation_discipline).
risk(objective_misalignment) :- weak(loss_function_documentation).
risk(non_reproducible_training) :- weak(seed_record); weak(checkpoint_record).
