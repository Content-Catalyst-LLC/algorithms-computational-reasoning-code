program negative_feedback_example
  implicit none
  integer :: i
  real :: x, target, gain
  x = 10.0
  target = 0.0
  gain = 0.2
  do i = 1, 5
    x = x - gain * (x - target)
  end do
  print *, "final_state=", x
end program negative_feedback_example
