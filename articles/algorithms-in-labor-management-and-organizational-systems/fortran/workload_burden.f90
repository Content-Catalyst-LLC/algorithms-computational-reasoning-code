program workload_burden_example
  implicit none
  real :: pace, hours, fatigue, schedule_volatility, burden
  pace = 0.84
  hours = 0.72
  fatigue = 0.70
  schedule_volatility = 0.78
  burden = (pace + hours + fatigue + schedule_volatility) / 4.0
  print *, "workload_burden_score=", burden
end program workload_burden_example
