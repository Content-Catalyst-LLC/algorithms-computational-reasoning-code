program hash_verification_demo
  implicit none
  character(len=*), parameter :: original = 'verified artifact manifest'
  character(len=*), parameter :: altered = 'verified artifact manifest!'
  print *, 'original checksum=', teaching_checksum(original)
  print *, 'altered checksum=', teaching_checksum(altered)
  print *, 'match=', teaching_checksum(original) == teaching_checksum(altered)
contains
  integer function teaching_checksum(s)
    character(len=*), intent(in) :: s
    integer :: i, total
    total = 0
    do i = 1, len_trim(s)
      total = mod(total + iachar(s(i:i)) * i, 1000003)
    end do
    teaching_checksum = total
  end function teaching_checksum
end program hash_verification_demo
