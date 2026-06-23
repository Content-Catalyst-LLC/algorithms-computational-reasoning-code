program formula_translation
  implicit none
  integer :: i
  real :: xs(6), x, y
  xs = (/ -2.0, -1.0, 0.0, 1.0, 2.0, 3.0 /)
  do i = 1, 6
    x = xs(i)
    y = 2.0*x*x - 3.0*x + 1.0
    print *, "x=", x, " y=", y
  end do
end program formula_translation
