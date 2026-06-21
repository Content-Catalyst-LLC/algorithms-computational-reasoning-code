program threshold_review
  implicit none
  real :: tp, fp, tn, fn, total
  tp = 80.0
  fp = 25.0
  tn = 140.0
  fn = 35.0
  total = tp + fp + tn + fn
  print '(A,F8.6)', 'accuracy=', (tp + tn) / total
  print '(A,F8.6)', 'precision=', tp / (tp + fp)
  print '(A,F8.6)', 'recall=', tp / (tp + fn)
end program threshold_review
