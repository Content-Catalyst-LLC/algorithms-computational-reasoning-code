program place_value_example
  implicit none
  integer :: digits(4), value, i
  digits = (/1, 2, 3, 0/)
  value = 0
  do i = 1, size(digits)
    value = value * 10 + digits(i)
  end do
  print *, "place_value=", value
end program place_value_example
