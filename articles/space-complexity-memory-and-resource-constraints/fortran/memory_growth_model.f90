program memory_growth_model
  integer :: v, e
  v = 1000
  e = 5000
  print '(A)', 'test_name value'
  print '(A,I0)', 'matrix_units ', v*v
  print '(A,I0)', 'adjacency_list_units ', v+e
end program memory_growth_model
