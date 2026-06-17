program decomposition_model
  implicit none
  integer :: i
  character(len=40), dimension(4) :: names
  real(8), dimension(4) :: subproblem, boundary, sequencing, dependencies, recomposition, score

  names = (/ 'Search system                          ', 'Public decision-support workflow       ', 'Scientific simulation                  ', 'Knowledge architecture                 ' /)
  subproblem = (/ 82.0d0, 74.0d0, 86.0d0, 80.0d0 /)
  boundary = (/ 78.0d0, 66.0d0, 82.0d0, 76.0d0 /)
  sequencing = (/ 82.0d0, 68.0d0, 80.0d0, 74.0d0 /)
  dependencies = (/ 72.0d0, 60.0d0, 78.0d0, 70.0d0 /)
  recomposition = (/ 72.0d0, 58.0d0, 82.0d0, 80.0d0 /)

  print '(A)', 'case_name decomposition_score warning'
  do i = 1, 4
    score(i) = 0.22d0*subproblem(i) + 0.20d0*boundary(i) + 0.18d0*sequencing(i) + 0.20d0*dependencies(i) + 0.20d0*recomposition(i)
    print '(A,1X,F8.3,1X,A)', trim(names(i)), score(i), 'Synthetic educational diagnostic only.'
  end do
end program decomposition_model
