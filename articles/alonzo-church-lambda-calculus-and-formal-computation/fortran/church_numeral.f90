program church_numeral_example
  implicit none
  integer :: i, x
  x = 0
  do i = 1, 3
    x = x + 1
  end do
  print *, "church_3_successor_0=", x
end program church_numeral_example
