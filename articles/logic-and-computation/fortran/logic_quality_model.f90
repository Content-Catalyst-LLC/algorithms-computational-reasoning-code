program logic_quality_model
  implicit none
  integer :: i
  character(len=36), dimension(4) :: names
  real(8), dimension(4) :: rule, predicate, traceq, test, governance, score

  names = (/ 'Input validation rules            ', 'Database query constraints        ', 'Decision-rule workflow            ', 'Program invariant checks          ' /)
  rule = (/ 82.0d0, 78.0d0, 74.0d0, 80.0d0 /)
  predicate = (/ 84.0d0, 80.0d0, 70.0d0, 78.0d0 /)
  traceq = (/ 68.0d0, 72.0d0, 68.0d0, 74.0d0 /)
  test = (/ 82.0d0, 76.0d0, 72.0d0, 80.0d0 /)
  governance = (/ 70.0d0, 72.0d0, 78.0d0, 66.0d0 /)

  print '(A)', 'case_name logic_quality warning'
  do i = 1, 4
    score(i) = 0.24d0*rule(i) + 0.24d0*predicate(i) + 0.20d0*traceq(i) + 0.18d0*test(i) + 0.14d0*governance(i)
    print '(A,1X,F8.3,1X,A)', trim(names(i)), score(i), 'Synthetic educational diagnostic only.'
  end do
end program logic_quality_model
