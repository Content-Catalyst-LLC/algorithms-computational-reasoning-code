program symbolic_rule_check
  implicit none
  logical :: has_documentation, logs_decisions, rule_fires
  has_documentation = .true.
  logs_decisions = .true.
  rule_fires = has_documentation .and. logs_decisions
  print *, "rule_fires=", rule_fires
end program symbolic_rule_check
