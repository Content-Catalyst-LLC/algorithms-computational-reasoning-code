program proportional_share_example
  implicit none
  real :: total
  real, dimension(3) :: weights, shares
  total = 1200.0
  weights = (/2.0, 1.0, 1.0/)
  shares = total * weights / sum(weights)
  print *, shares
end program proportional_share_example
