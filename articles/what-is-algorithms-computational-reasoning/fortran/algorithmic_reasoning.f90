program algorithmic_reasoning
  implicit none
  integer :: i
  character(len=40), dimension(4) :: names
  real(8), dimension(4) :: representation, correctness, governance, brute_force, score

  names = (/ 'Brute-force procedure              ', 'Indexed search design              ', 'Graph-aware reasoning              ', 'Governed computational reasoning   ' /)
  representation = (/ 40.0d0, 62.0d0, 76.0d0, 86.0d0 /)
  correctness = (/ 28.0d0, 52.0d0, 68.0d0, 82.0d0 /)
  governance = (/ 20.0d0, 38.0d0, 54.0d0, 86.0d0 /)
  brute_force = (/ 92.0d0, 42.0d0, 30.0d0, 18.0d0 /)

  print '(A)', 'scenario reasoning_score warning'
  do i = 1, 4
    score(i) = max(0.0d0, min(100.0d0, 0.30d0*representation(i) + 0.30d0*correctness(i) + 0.30d0*governance(i) - 0.10d0*brute_force(i)))
    print '(A,1X,F8.3,1X,A)', trim(names(i)), score(i), 'Synthetic governance diagnostic only.'
  end do
end program algorithmic_reasoning
