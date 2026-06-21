program counterfactual_threshold
  implicit none
  real :: original, counterfactual, threshold
  original = 0.57
  counterfactual = 0.65
  threshold = 0.62
  print *, 'original_favorable=', original >= threshold
  print *, 'counterfactual_favorable=', counterfactual >= threshold
  print *, 'decision_flipped=', (original < threshold) .and. (counterfactual >= threshold)
end program counterfactual_threshold
