program measurement_review
  implicit none
  real :: errors, total
  errors = 180.0
  total = 900.0
  print '(A,F6.4)', 'label_disagreement_rate=', errors / total
end program measurement_review
