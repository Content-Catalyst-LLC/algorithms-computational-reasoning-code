program route_distance_example
  implicit none
  real, dimension(3) :: segments
  segments = (/12.0, 20.0, 7.5/)
  print *, "segments=", size(segments)
  print *, "total_distance=", sum(segments)
end program route_distance_example
