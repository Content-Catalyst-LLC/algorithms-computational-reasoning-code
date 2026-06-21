program agent_permission
  implicit none
  real :: risk
  logical :: approval_required, approved
  character(len=20) :: status
  risk = 0.85
  approval_required = .true.
  approved = .false.
  status = "pass"
  if (approval_required .and. .not. approved) then
    status = "blocked"
  else if (risk >= 0.65) then
    status = "escalate"
  end if
  print *, "agent_action_status=", trim(status)
end program agent_permission
