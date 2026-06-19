program search_model
  integer :: i, b, d, total, pow
  b = 3; d = 5; total = 0; pow = 1
  do i = 0, d
     if (i == 0) then
        pow = 1
     else
        pow = pow * b
     endif
     total = total + pow
  end do
  print '(A)', 'test_name value'
  print '(A,I10)', 'branching_state_count ', total
  print '(A,F10.3)', 'path_cost ', 11.5
  print '(A,F10.3)', 'heuristic_score ', 13.5
  print '(A,F10.6)', 'coverage_ratio ', 850.0 / 5000.0
  print '(A,F10.6)', 'pruning_ratio ', 1200.0 / 4200.0
end program search_model
