program numerical_approximation
  implicit none
  real(8) :: x, h, estimate
  x = 1.0d0
  h = 0.01d0
  estimate = (f(x + h) - f(x - h)) / (2.0d0 * h)
  print '(F16.12)', estimate
contains
  real(8) function f(x)
    real(8), intent(in) :: x
    f = sin(x) + 0.25d0 * x * x
  end function f
end program numerical_approximation
