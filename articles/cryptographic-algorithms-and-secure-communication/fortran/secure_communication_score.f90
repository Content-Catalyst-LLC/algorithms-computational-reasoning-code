program secure_communication_score
  implicit none
  real :: standard_score, legacy_score
  standard_score = 100.0 * (0.22 * 0.86 + 0.24 * 0.82 + 0.18 * 0.90 + 0.18 * 0.86 + 0.18 * 0.84)
  legacy_score = 100.0 * (0.22 * 0.36 + 0.24 * 0.24 + 0.18 * 0.18 + 0.18 * 0.34 + 0.18 * 0.28)
  print *, 'standard secure channel score=', standard_score
  print *, 'legacy manual transfer score=', legacy_score
end program secure_communication_score
