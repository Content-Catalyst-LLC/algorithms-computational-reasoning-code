program threshold_action_example
  implicit none
  real :: level, threshold
  logical :: triggered
  level = 7.5
  threshold = 5.0
  triggered = level >= threshold
  print *, "action_triggered=", triggered
end program threshold_action_example
