program schema_score_model
  real :: score
  score = 100.0 * (0.22*0.90 + 0.20*0.85 + 0.20*0.80 + 0.20*0.88 + 0.18*0.82)
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'schema_quality_score ', score
end program schema_score_model
