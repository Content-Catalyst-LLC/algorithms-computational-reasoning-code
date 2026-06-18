program cloud_model
  real :: total_latency, capacity, cost
  total_latency = 80.0 + 45.0 + 60.0 + 25.0 + 15.0
  capacity = 12.0 * 250.0
  cost = (120.0 + 35.0 + 25.0 + 90.0 + 18.0) / 144000.0
  print '(A)', 'test_name value'
  print '(A,F10.3)', 'cloud_response_latency_ms ', total_latency
  print '(A,F10.3)', 'nominal_capacity ', capacity
  print '(A,F10.6)', 'unit_cost ', cost
end program cloud_model
