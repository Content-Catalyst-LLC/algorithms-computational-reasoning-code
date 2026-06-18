program complexity_growth_model
  real :: n
  n = 1000.0
  print '(A)', 'test_name value'
  print '(A)', 'linear_1000 1000'
  print '(A,F12.6)', 'nlogn_1000 ', n * log(n) / log(2.0)
  print '(A)', 'quadratic_1000 1000000'
end program complexity_growth_model
