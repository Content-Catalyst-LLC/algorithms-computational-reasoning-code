program learning_gain_example
  implicit none
  real :: pretest, posttest, gain
  pretest = 0.52
  posttest = 0.78
  gain = posttest - pretest
  print *, "learning_gain=", gain
end program learning_gain_example
