program literacy_gap_model
  implicit none
  integer :: i
  character(len=40), dimension(4) :: names
  real(8), dimension(4) :: transparency, interpretability, contestability, governance, judgment, score

  names = (/ 'Search ranking                          ', 'Public decision-support workflow       ', 'Scientific simulation dashboard        ', 'Recommendation feed                    ' /)
  transparency = (/ 62.0d0, 58.0d0, 76.0d0, 40.0d0 /)
  interpretability = (/ 66.0d0, 56.0d0, 74.0d0, 48.0d0 /)
  contestability = (/ 38.0d0, 70.0d0, 60.0d0, 32.0d0 /)
  governance = (/ 52.0d0, 76.0d0, 68.0d0, 46.0d0 /)
  judgment = (/ 68.0d0, 74.0d0, 80.0d0, 50.0d0 /)

  print '(A)', 'case_name literacy_support_score warning'
  do i = 1, 4
    score(i) = 0.22d0*transparency(i) + 0.22d0*interpretability(i) + 0.18d0*contestability(i) + 0.18d0*governance(i) + 0.20d0*judgment(i)
    print '(A,1X,F8.3,1X,A)', trim(names(i)), score(i), 'Synthetic educational diagnostic only.'
  end do
end program literacy_gap_model
