program evaluation_metric
  implicit none
  real :: tp, tn, fp, fn, accuracy
  tp = 42.0
  tn = 38.0
  fp = 7.0
  fn = 13.0
  accuracy = (tp + tn) / (tp + tn + fp + fn)
  print *, "accuracy=", accuracy
end program evaluation_metric
