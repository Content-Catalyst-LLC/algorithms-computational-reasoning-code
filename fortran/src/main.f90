program acr_fortran_demo
  implicit none
  integer :: i
  do i = 0, 6
     print *, i, factorial(i)
  end do
contains
  recursive function factorial(n) result(res)
    integer, intent(in) :: n
    integer :: res
    if (n == 0) then
      res = 1
    else
      res = n * factorial(n - 1)
    end if
  end function factorial
end program acr_fortran_demo
