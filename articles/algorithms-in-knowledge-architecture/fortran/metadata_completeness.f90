program metadata_completeness
  implicit none
  real :: present_fields, required_fields, score
  present_fields = 11.0
  required_fields = 12.0
  score = present_fields / required_fields
  print *, "metadata_completeness_score=", score
end program metadata_completeness
