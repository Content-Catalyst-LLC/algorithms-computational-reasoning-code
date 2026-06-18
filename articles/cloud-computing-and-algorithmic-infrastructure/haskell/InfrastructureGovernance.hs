module InfrastructureGovernance where
data GovernanceControl = LeastPrivilege | InfrastructureAsCode | CostAlert | BackupTest | DependencyMap | IncidentRunbook deriving (Eq, Show)
