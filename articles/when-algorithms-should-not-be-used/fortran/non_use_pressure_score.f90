program non_use_pressure_score
  implicit none
  real, dimension(4) :: scores
  real :: pressure
  scores = (/0.94, 0.78, 0.56, 0.70/)
  pressure = sum(scores) / 4.0
  print *, "non_use_pressure_score=", pressure
end program non_use_pressure_score
