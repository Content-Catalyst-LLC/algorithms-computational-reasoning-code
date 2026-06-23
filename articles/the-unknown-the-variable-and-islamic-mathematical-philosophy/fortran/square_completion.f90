program square_completion_example
  implicit none
  real :: b, c, completion
  b = 10.0
  c = 39.0
  completion = (b / 2.0) ** 2
  print *, "completion_term=", completion
  print *, "completed_rhs=", c + completion
end program square_completion_example
