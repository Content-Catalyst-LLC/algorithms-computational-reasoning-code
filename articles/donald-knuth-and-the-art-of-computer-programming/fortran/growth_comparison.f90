program growth_comparison
  implicit none
  real :: n
  n = 1000.0
  print *, "log2_n=", log(n) / log(2.0)
  print *, "n=", n
  print *, "n_log2_n=", n * log(n) / log(2.0)
  print *, "n_squared=", n * n
end program growth_comparison
