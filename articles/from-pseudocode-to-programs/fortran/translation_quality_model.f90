program translation_quality_model
  implicit none
  integer :: i
  character(len=36), dimension(4) :: names
  real(8), dimension(4) :: intent, control, edge, tests, maintain, score

  names = (/ 'Search ranking prototype          ', 'Decision-rule implementation      ', 'Simulation loop                   ', 'Data-cleaning procedure           ' /)
  intent = (/ 82.0d0, 76.0d0, 84.0d0, 78.0d0 /)
  control = (/ 80.0d0, 74.0d0, 82.0d0, 76.0d0 /)
  edge = (/ 64.0d0, 66.0d0, 72.0d0, 70.0d0 /)
  tests = (/ 68.0d0, 62.0d0, 70.0d0, 66.0d0 /)
  maintain = (/ 72.0d0, 68.0d0, 74.0d0, 72.0d0 /)

  print '(A)', 'case_name translation_quality warning'
  do i = 1, 4
    score(i) = 0.22d0*intent(i) + 0.22d0*control(i) + 0.18d0*edge(i) + 0.18d0*tests(i) + 0.20d0*maintain(i)
    print '(A,1X,F8.3,1X,A)', trim(names(i)), score(i), 'Synthetic educational diagnostic only.'
  end do
end program translation_quality_model
