program lp_grid
  implicit none
  integer :: x, y, bx, by, bv, value
  bx = 0; by = 0; bv = -1
  do x = 0, 9
    do y = 0, 9
      if (2*x + y <= 8 .and. x + 2*y <= 8) then
        value = 3*x + 4*y
        if (value > bv) then
          bx = x; by = y; bv = value
        end if
      end if
    end do
  end do
  print *, "best x=", bx, " y=", by, " objective=", bv
end program lp_grid
