program data_quality_model
  real :: missingness_rate, completeness_score, quality
  missingness_rate = 45.0 / 1000.0
  completeness_score = 1.0 - missingness_rate
  quality = 100.0 * (0.25*0.92 + 0.20*0.88 + 0.15*0.86 + 0.22*0.90 + 0.18*0.89)
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'missingness_rate_45_of_1000 ', missingness_rate
  print '(A,F10.6)', 'completeness_score_45_of_1000 ', completeness_score
  print '(A,F10.6)', 'data_quality_score ', quality
end program data_quality_model
