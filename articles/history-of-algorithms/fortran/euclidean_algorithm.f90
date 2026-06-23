program euclidean_algorithm_example
  implicit none
  integer :: a, b, r
  a = 252
  b = 105
  do while (b /= 0)
    r = mod(a, b)
    a = b
    b = r
  end do
  print *, "gcd=", abs(a)
end program euclidean_algorithm_example
