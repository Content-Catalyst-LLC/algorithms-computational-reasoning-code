program boundary_state_model
  implicit none
  integer :: i
  character(len=36), dimension(4) :: names
  real(8), dimension(4) :: input, output, state, stopping, failure, score

  names = (/ 'Graph traversal                    ', 'Decision-support workflow          ', 'Numerical simulation               ', 'Recommendation ranking             ' /)
  input = (/ 84.0d0, 68.0d0, 82.0d0, 74.0d0 /)
  output = (/ 80.0d0, 70.0d0, 78.0d0, 72.0d0 /)
  state = (/ 86.0d0, 74.0d0, 84.0d0, 70.0d0 /)
  stopping = (/ 80.0d0, 62.0d0, 78.0d0, 60.0d0 /)
  failure = (/ 70.0d0, 60.0d0, 66.0d0, 52.0d0 /)

  print '(A)', 'case_name boundary_score warning'
  do i = 1, 4
    score(i) = 0.22d0*input(i) + 0.22d0*output(i) + 0.22d0*state(i) + 0.20d0*stopping(i) + 0.14d0*failure(i)
    print '(A,1X,F8.3,1X,A)', trim(names(i)), score(i), 'Synthetic educational diagnostic only.'
  end do
end program boundary_state_model
