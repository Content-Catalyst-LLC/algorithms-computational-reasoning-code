program tradeoff_model
  real :: baseline, optimized, gain
  baseline = 100.0
  optimized = 64.0
  gain = (baseline - optimized) / baseline
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'efficiency_gain_percent ', 100.0 * gain
end program tradeoff_model
