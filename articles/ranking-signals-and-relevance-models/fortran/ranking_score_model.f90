program ranking_score_model
  real :: precision_at_3, ranking_score
  precision_at_3 = 2.0 / 3.0
  ranking_score = 100.0 * (0.22*0.84 + 0.18*0.88 + 0.12*0.76 + 0.16*0.82 + 0.17*0.78 + 0.15*0.86)
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'precision_at_3 ', precision_at_3
  print '(A,F10.6)', 'ranking_signal_score ', ranking_score
end program ranking_score_model
