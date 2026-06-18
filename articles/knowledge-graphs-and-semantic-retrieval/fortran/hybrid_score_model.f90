program hybrid_score_model
  real :: hybrid_score, path_score, length_factor
  hybrid_score = 100.0 * (0.25*0.82 + 0.25*0.78 + 0.25*0.88 + 0.25*0.90)
  length_factor = 1.0 / (1.0 + max(3.0 - 1.0, 0.0))
  path_score = 100.0 * (0.25*length_factor + 0.30*0.90 + 0.30*0.92 + 0.15*0.95)
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'hybrid_score ', hybrid_score
  print '(A,F10.6)', 'graph_path_score ', path_score
end program hybrid_score_model
