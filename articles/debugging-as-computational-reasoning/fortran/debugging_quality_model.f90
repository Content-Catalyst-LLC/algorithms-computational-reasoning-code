program debugging_quality_model
  implicit none
  integer :: i
  character(len=40), dimension(4) :: names
  real(8), dimension(4) :: reproduce, traceq, isolate, verify, regression, score

  names = (/ 'Graph traversal infinite loop        ', 'Data pipeline missing-value bug     ', 'Simulation instability              ', 'Recommendation ranking tie bug      ' /)
  reproduce = (/ 88.0d0, 84.0d0, 80.0d0, 76.0d0 /)
  traceq = (/ 78.0d0, 74.0d0, 78.0d0, 68.0d0 /)
  isolate = (/ 80.0d0, 72.0d0, 70.0d0, 70.0d0 /)
  verify = (/ 82.0d0, 76.0d0, 74.0d0, 72.0d0 /)
  regression = (/ 78.0d0, 74.0d0, 66.0d0, 70.0d0 /)

  print '(A)', 'case_name debugging_quality warning'
  do i = 1, 4
    score(i) = 0.22d0*reproduce(i) + 0.20d0*traceq(i) + 0.18d0*isolate(i) + 0.22d0*verify(i) + 0.18d0*regression(i)
    print '(A,1X,F8.3,1X,A)', trim(names(i)), score(i), 'Synthetic educational diagnostic only.'
  end do
end program debugging_quality_model
