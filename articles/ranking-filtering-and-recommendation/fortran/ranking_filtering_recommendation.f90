program ranking_filtering_recommendation
  implicit none
  real :: score
  score = 0.36*0.92 + 0.30*0.88 + 0.16*0.60 + 0.14*0.35 - 0.20*0.04
  print '(F8.6)', score
end program ranking_filtering_recommendation
