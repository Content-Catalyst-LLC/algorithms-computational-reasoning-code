program performance_model
  real :: response_time, throughput, utilization, little_law
  response_time = 45.0 + 20.0 + 85.0 + 35.0 + 15.0
  throughput = 12000.0 / 60.0
  utilization = 180.0 / 200.0
  little_law = 180.0 * 0.45
  print '(A)', 'test_name value'
  print '(A,F10.3)', 'response_time_ms ', response_time
  print '(A,F10.3)', 'throughput ', throughput
  print '(A,F10.3)', 'utilization ', utilization
  print '(A,F10.3)', 'little_law_items ', little_law
end program performance_model
