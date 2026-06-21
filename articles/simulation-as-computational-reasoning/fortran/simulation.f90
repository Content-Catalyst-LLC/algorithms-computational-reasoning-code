program simulation_as_computational_reasoning
  implicit none
  integer :: t
  real :: stock
  stock = 100.0
  do t = 0, 30
    print *, 'time_step=', t, ' stock=', stock
    stock = max(0.0, stock + 0.08 * stock - 0.03 * stock - 0.04 * stock)
  end do
end program simulation_as_computational_reasoning
