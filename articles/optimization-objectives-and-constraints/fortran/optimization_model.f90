program optimization_model
  real :: objective, margin, penalty_obj, trade
  objective = 4.0*10.0 + 2.0*20.0 + 1.5*5.0
  margin = 100.0 - 86.5
  penalty_obj = 42.0 + 2.5*8.0
  trade = 0.35*(1.0-0.30) + 0.40*0.82 + 0.25*(1.0-0.25)
  print '(A)', 'test_name value'
  print '(A,F10.3)', 'linear_objective ', objective
  print '(A,F10.3)', 'constraint_margin ', margin
  print '(A,F10.3)', 'penalty_objective ', penalty_obj
  print '(A,F10.6)', 'normalized_tradeoff_score ', trade
end program optimization_model
