program platform_model
  real :: dependency, switchcost, api_ratio, visibility
  dependency = 100.0 * (0.22*0.80 + 0.22*0.90 + 0.18*0.70 + 0.24*0.85 + 0.14*0.65)
  switchcost = 45000.0 + 120000.0 + 18000.0 + 24000.0 + 75000.0
  api_ratio = 850000.0 / 1000000.0
  visibility = 250000.0 / 5000000.0
  print '(A)', 'test_name value'
  print '(A,F10.3)', 'dependency_score ', dependency
  print '(A,F10.3)', 'switching_cost ', switchcost
  print '(A,F10.6)', 'api_dependency_ratio ', api_ratio
  print '(A,F10.6)', 'visibility_share ', visibility
end program platform_model
