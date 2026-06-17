program abstraction_model
  implicit none
  integer :: i
  character(len=32), dimension(4) :: names
  real(8), dimension(4) :: clarity, scope, detail, interpretation, governance, score

  names = (/ 'Search ranking                  ', 'Transit model                   ', 'Database schema                 ', 'Decision-support score          ' /)
  clarity = (/ 82.0d0, 78.0d0, 84.0d0, 70.0d0 /)
  scope = (/ 70.0d0, 72.0d0, 78.0d0, 60.0d0 /)
  detail = (/ 62.0d0, 66.0d0, 70.0d0, 48.0d0 /)
  interpretation = (/ 60.0d0, 72.0d0, 74.0d0, 52.0d0 /)
  governance = (/ 56.0d0, 66.0d0, 70.0d0, 66.0d0 /)

  print '(A)', 'case_name abstraction_score warning'
  do i = 1, 4
    score(i) = 0.22d0*clarity(i) + 0.20d0*scope(i) + 0.20d0*detail(i) + 0.23d0*interpretation(i) + 0.15d0*governance(i)
    print '(A,1X,F8.3,1X,A)', trim(names(i)), score(i), 'Synthetic educational diagnostic only.'
  end do
end program abstraction_model
