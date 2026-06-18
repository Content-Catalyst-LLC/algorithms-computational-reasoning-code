program query_score_model
  real :: score
  score = 100.0 * (0.18*0.88 + 0.18*0.86 + 0.18*0.84 + 0.18*0.82 + 0.14*0.84 + 0.14*0.80)
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'query_logic_core_score ', score
end program query_score_model
