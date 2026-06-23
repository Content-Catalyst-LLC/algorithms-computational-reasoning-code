program fetch_execute_example
  implicit none
  integer :: acc
  acc = 0
  acc = 2
  acc = acc + 3
  print *, "store address=0 value=", acc
  print *, "halt accumulator=", acc
end program fetch_execute_example
