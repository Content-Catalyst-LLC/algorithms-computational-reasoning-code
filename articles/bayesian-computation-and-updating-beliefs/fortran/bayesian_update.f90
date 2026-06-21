program bayesian_update
  implicit none
  real :: post_alpha, post_beta
  post_alpha = 2.0 + 113.0
  post_beta = 2.0 + 72.0
  print *, "posterior_mean=", post_alpha / (post_alpha + post_beta)
end program bayesian_update
