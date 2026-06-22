program fairness_gap_score
  implicit none
  real, dimension(3) :: rates
  real :: selection_gap
  rates = (/0.42, 0.31, 0.36/)
  selection_gap = maxval(rates) - minval(rates)
  print *, "selection_gap=", selection_gap
end program fairness_gap_score
