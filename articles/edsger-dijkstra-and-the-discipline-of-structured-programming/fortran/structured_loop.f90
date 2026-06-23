program structured_loop
  implicit none
  integer :: i, acc
  acc = 0
  do i = 0, 5
    acc = acc + i
  end do
  print *, "sum_to_5=", acc
end program structured_loop
