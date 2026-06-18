program streaming_queue_model
  real :: arrival, processing, utilization
  arrival = 90.0
  processing = 100.0
  utilization = arrival / processing
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'utilization ', utilization
end program streaming_queue_model
