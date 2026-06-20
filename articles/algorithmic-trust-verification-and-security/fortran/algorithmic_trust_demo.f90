program algorithmic_trust_demo
  implicit none
  real :: score
  score = 100.0 * (0.18*0.88 + 0.18*0.82 + 0.18*0.88 + 0.16*0.90 + 0.15*0.84 + 0.15*0.82)
  print '(A,F6.3)', 'trust quality=', score
end program algorithmic_trust_demo
