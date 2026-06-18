program cardinality_model
  real :: selection_estimate, join_estimate
  selection_estimate = 1000000.0 * 0.012
  join_estimate = (500000.0 * 200000.0) / max(50000.0, 40000.0)
  print '(A)', 'test_name value'
  print '(A,F12.3)', 'selection_estimated_rows ', selection_estimate
  print '(A,F12.3)', 'join_estimated_rows ', join_estimate
end program cardinality_model
