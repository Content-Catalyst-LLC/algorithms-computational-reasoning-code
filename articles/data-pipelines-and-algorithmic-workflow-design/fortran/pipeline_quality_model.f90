program pipeline_quality_model
  real :: freshness, quality
  freshness = exp(-0.025 * 3.0)
  quality = 100.0 * (0.25*0.92 + 0.18*0.86 + 0.20*0.90 + 0.22*0.88 + 0.15*0.82)
  print '(A)', 'test_name value'
  print '(A,F10.6)', 'freshness_3_days ', freshness
  print '(A,F10.6)', 'pipeline_quality_score ', quality
end program pipeline_quality_model
