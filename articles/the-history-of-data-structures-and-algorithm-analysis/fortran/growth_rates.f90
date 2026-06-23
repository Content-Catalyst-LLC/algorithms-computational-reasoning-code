program growth_rates
  implicit none
  integer :: i
  real :: ns(4), n
  ns = (/ 10.0, 100.0, 1000.0, 10000.0 /)
  do i = 1, 4
    n = ns(i)
    print *, "n=", n, " log2=", log(n)/log(2.0), " nlogn=", n*log(n)/log(2.0), " n2=", n*n
  end do
end program growth_rates
