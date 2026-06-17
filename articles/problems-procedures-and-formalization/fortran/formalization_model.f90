program formalization_model
  implicit none
  integer :: i
  character(len=32), dimension(4) :: names
  real(8), dimension(4) :: input, output, objective, assumptions, governance, score

  names = (/ 'Document search                 ', 'Worker scheduling              ', 'Public service triage          ', 'Scientific simulation          ' /)
  input = (/ 82.0d0, 72.0d0, 60.0d0, 86.0d0 /)
  output = (/ 78.0d0, 76.0d0, 72.0d0, 80.0d0 /)
  objective = (/ 70.0d0, 58.0d0, 52.0d0, 76.0d0 /)
  assumptions = (/ 58.0d0, 54.0d0, 46.0d0, 84.0d0 /)
  governance = (/ 56.0d0, 62.0d0, 66.0d0, 70.0d0 /)

  print '(A)', 'case_name formalization_score warning'
  do i = 1, 4
    score(i) = 0.20d0*input(i) + 0.20d0*output(i) + 0.25d0*objective(i) + 0.20d0*assumptions(i) + 0.15d0*governance(i)
    print '(A,1X,F8.3,1X,A)', trim(names(i)), score(i), 'Synthetic educational diagnostic only.'
  end do
end program formalization_model
