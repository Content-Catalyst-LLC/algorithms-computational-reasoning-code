program speedup_model
  real :: s, p, speed
  s = 0.10
  p = 16.0
  speed = 1.0 / (s + ((1.0 - s) / p))
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'speedup_p16_s010 ', speed
  print '(A,F10.6)', 'efficiency_p16_s010 ', speed / p
end program speedup_model
