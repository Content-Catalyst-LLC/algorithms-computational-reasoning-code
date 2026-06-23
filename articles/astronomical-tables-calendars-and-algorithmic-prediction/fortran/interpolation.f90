program interpolation_example
  implicit none
  real :: x0, y0, x1, y1, x, y
  x0 = 10.0
  y0 = 1.2
  x1 = 20.0
  y1 = 2.8
  x = 15.0
  y = y0 + ((x - x0) / (x1 - x0)) * (y1 - y0)
  print *, "interpolated_y=", y
end program interpolation_example
