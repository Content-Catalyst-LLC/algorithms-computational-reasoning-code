program scientific_computing
  implicit none
  integer :: i, n
  real(8) :: a, b, h, total, x
  n = 200
  a = 0.0d0
  b = acos(-1.0d0)
  h = (b - a) / dble(n)
  total = 0.5d0 * (sin(a) + sin(b))
  do i = 1, n - 1
     x = a + dble(i) * h
     total = total + sin(x)
  end do
  print *, 'trapezoid_integral=', h * total
end program scientific_computing
