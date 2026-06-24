program threshold_unit_example
  implicit none
  integer :: inputs(2), weights(2), total, output
  inputs = (/ 1, 1 /)
  weights = (/ 1, 1 /)
  total = sum(inputs * weights)
  if (total >= 2) then
    output = 1
  else
    output = 0
  end if
  print *, output
end program threshold_unit_example
