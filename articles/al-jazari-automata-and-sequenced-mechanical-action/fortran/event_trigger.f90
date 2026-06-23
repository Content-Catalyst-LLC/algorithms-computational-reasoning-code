program event_trigger_example
  implicit none
  real :: value, trigger
  logical :: event_triggered
  value = 12.0
  trigger = 10.0
  event_triggered = value >= trigger
  print *, "event_triggered=", event_triggered
end program event_trigger_example
