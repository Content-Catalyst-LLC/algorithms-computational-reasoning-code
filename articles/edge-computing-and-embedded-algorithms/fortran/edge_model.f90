program edge_model
  real :: edge_time, cloud_time, life
  edge_time = 8.0 + 6.0 + 14.0 + 5.0
  cloud_time = 8.0 + 90.0 + 60.0 + 90.0 + 5.0
  life = 12.0 / 0.08
  print '(A)', 'test_name value'
  print '(A,F10.3)', 'edge_response_time_ms ', edge_time
  print '(A,F10.3)', 'cloud_response_time_ms ', cloud_time
  print '(A,F10.3)', 'battery_life_hours ', life
end program edge_model
