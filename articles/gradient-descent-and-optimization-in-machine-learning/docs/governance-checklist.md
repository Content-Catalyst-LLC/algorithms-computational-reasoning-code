# Gradient Descent and Machine Learning Optimization Governance Checklist

Use this checklist when reviewing model training workflows.

## Objective and loss

- Is the training objective documented?
- Does the loss function align with the system purpose?
- Are class weights, penalty weights, or ranking weights justified?
- Are proxy objectives identified and reviewed?

## Data and features

- Is data lineage recorded?
- Are train, validation, and test splits documented?
- Are leakage risks reviewed?
- Are scaling, encoding, and normalization steps recorded?

## Optimizer and training process

- Is the optimizer documented?
- Is the learning rate or schedule justified?
- Are random seeds, checkpoints, and versions stored?
- Are training and validation traces preserved?

## Generalization and risk

- Is overfitting monitored?
- Are calibration, robustness, and drift evaluated?
- Are fairness and distributional error effects reviewed?
- Are model limitations communicated before deployment?
