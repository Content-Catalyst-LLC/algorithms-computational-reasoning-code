program proxy_measurement_risk
  implicit none
  real :: validity_gap, missingness, differential_error, label_error, score
  validity_gap = 0.42
  missingness = 0.12
  differential_error = 0.24
  label_error = 0.08
  score = (validity_gap + missingness + differential_error + label_error) / 4.0
  print *, "measurement_risk_score=", score
end program proxy_measurement_risk
