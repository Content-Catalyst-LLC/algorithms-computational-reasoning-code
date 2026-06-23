program frequency_count_example
  implicit none
  character(len=*), parameter :: text = "THIS IS A TOY CLASSICAL CIPHER EXAMPLE"
  integer :: counts(26)
  integer :: i, idx, code
  character :: ch

  counts = 0
  do i = 1, len_trim(text)
     ch = text(i:i)
     code = iachar(ch)
     if (code >= iachar('A') .and. code <= iachar('Z')) then
        idx = code - iachar('A') + 1
        counts(idx) = counts(idx) + 1
     end if
  end do

  do i = 1, 26
     if (counts(i) > 0) print *, achar(iachar('a') + i - 1), counts(i)
  end do
end program frequency_count_example
