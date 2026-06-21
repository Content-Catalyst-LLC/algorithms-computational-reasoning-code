program supervised_unsupervised_rl_example
  implicit none
  real :: train, test
  train = 0.82
  test = 0.74
  print *, "generalization_gap=", train - test
end program supervised_unsupervised_rl_example
