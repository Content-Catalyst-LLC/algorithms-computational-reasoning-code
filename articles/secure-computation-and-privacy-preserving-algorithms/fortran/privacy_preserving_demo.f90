program privacy_preserving_demo
  implicit none
  real :: weights(3)
  integer :: counts(3)
  real :: weighted
  integer :: total

  weights = (/0.42, 0.55, 0.49/)
  counts = (/100, 240, 160/)
  weighted = sum(weights * real(counts))
  total = sum(counts)

  print *, 'federated average weight=', weighted / real(total)
end program privacy_preserving_demo
