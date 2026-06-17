program reasoning_profiles
  implicit none
  integer :: i
  character(len=40), dimension(5) :: names
  real(8), dimension(5) :: step, decomp, control, test, representation, governance, algorithmic, computational

  names = (/ 'Recipe-like procedure                 ', 'Classroom algorithm exercise         ', 'Search and ranking system            ', 'Public decision-support workflow     ', 'Scientific modeling workflow         ' /)
  step = (/ 86.0d0, 90.0d0, 72.0d0, 68.0d0, 74.0d0 /)
  decomp = (/ 72.0d0, 82.0d0, 70.0d0, 66.0d0, 78.0d0 /)
  control = (/ 70.0d0, 84.0d0, 76.0d0, 64.0d0, 76.0d0 /)
  test = (/ 62.0d0, 78.0d0, 66.0d0, 72.0d0, 82.0d0 /)
  representation = (/ 42.0d0, 62.0d0, 78.0d0, 80.0d0, 86.0d0 /)
  governance = (/ 20.0d0, 32.0d0, 70.0d0, 86.0d0, 74.0d0 /)

  print '(A)', 'name algorithmic_score computational_score warning'
  do i = 1, 5
    algorithmic(i) = 0.28d0*step(i) + 0.24d0*decomp(i) + 0.24d0*control(i) + 0.24d0*test(i)
    computational(i) = 0.16d0*step(i) + 0.14d0*decomp(i) + 0.14d0*control(i) + 0.14d0*test(i) + 0.22d0*representation(i) + 0.20d0*governance(i)
    print '(A,1X,F8.3,1X,F8.3,1X,A)', trim(names(i)), algorithmic(i), computational(i), 'Synthetic educational diagnostic only.'
  end do
end program reasoning_profiles
