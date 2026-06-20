program threshold_classifier
  implicit none
  real :: score, threshold
  integer :: label
  score = 0.72
  threshold = 0.50
  if (score >= threshold) then
    label = 1
  else
    label = 0
  end if
  print *, label
end program threshold_classifier
