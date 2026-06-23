program entropy_example
  implicit none
  real :: p1, p2, h
  p1 = 0.5
  p2 = 0.5
  h = -(p1 * log(p1) / log(2.0) + p2 * log(p2) / log(2.0))
  print *, "entropy_bits=", h
end program entropy_example
