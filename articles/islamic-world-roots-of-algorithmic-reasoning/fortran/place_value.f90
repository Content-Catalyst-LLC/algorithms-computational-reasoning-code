program place_value_example
  implicit none
  integer :: digit, base, position, value
  digit = 7
  base = 10
  position = 3
  value = digit * base**position
  print *, "place_value=", value
end program place_value_example
