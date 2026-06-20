program gradient_descent
  implicit none
  real :: x(5) = (/ -2.0, -1.0, 0.0, 1.0, 2.0 /)
  real :: y(5) = (/ -2.85, -0.67, 1.47, 3.63, 5.82 /)
  real :: w, b, eta, grad_w, grad_b, err, loss
  integer :: i, step

  w = 0.0
  b = 0.0
  eta = 0.08

  do step = 1, 80
    grad_w = 0.0
    grad_b = 0.0
    do i = 1, 5
      err = (w*x(i) + b) - y(i)
      grad_w = grad_w + (2.0/5.0) * err * x(i)
      grad_b = grad_b + (2.0/5.0) * err
    end do
    w = w - eta * grad_w
    b = b - eta * grad_b
  end do

  loss = 0.0
  do i = 1, 5
    loss = loss + (y(i) - (w*x(i)+b))**2
  end do
  loss = loss / 5.0

  print *, 'weight=', w, ' bias=', b, ' loss=', loss
end program gradient_descent
