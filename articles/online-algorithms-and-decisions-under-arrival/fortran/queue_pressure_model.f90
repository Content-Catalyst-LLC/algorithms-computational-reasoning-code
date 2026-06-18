program queue_pressure_model
  real :: arrival, service, utilization
  arrival = 95.0
  service = 100.0
  utilization = arrival / service
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'utilization ', utilization
end program queue_pressure_model
