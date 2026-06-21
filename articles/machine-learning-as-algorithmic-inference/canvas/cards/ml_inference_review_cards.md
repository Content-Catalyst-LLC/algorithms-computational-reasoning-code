# Machine-Learning Inference Review Cards

## Card 1: Feature Review

**Claim:** Features make the case legible to the model.  
**Review question:** Do these features validly represent the phenomenon being modeled?  
**Artifact:** `outputs/tables/ml_feature_label_audit.csv`

## Card 2: Threshold Review

**Claim:** Thresholds convert scores into actions.  
**Review question:** Who selected the threshold and what harms does it trade off?  
**Artifact:** `outputs/tables/ml_threshold_sweep.csv`

## Card 3: Calibration Review

**Claim:** Scores are often interpreted as probabilities.  
**Review question:** Do observed rates match predicted scores?  
**Artifact:** `outputs/tables/ml_calibration_bins.csv`

## Card 4: Subgroup Error Review

**Claim:** Average performance can hide uneven error burdens.  
**Review question:** Which groups experience higher false positive or false negative rates?  
**Artifact:** `outputs/tables/ml_group_error_diagnostics.csv`
