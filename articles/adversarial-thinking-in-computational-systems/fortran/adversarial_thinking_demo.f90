program adversarial_thinking_demo
  implicit none
  real :: threat, surface, monitoring, defense, incident, governance, score
  threat = 0.86
  surface = 0.82
  monitoring = 0.88
  defense = 0.82
  incident = 0.80
  governance = 0.78
  score = 100.0 * (0.18*threat + 0.18*surface + 0.18*monitoring + 0.18*defense + 0.14*incident + 0.14*governance)
  print *, 'adversarial readiness=', score
end program adversarial_thinking_demo
