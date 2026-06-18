module WorkflowDesign where
data WorkflowControl = Contract | Dependency | Idempotence | Lineage | GovernanceGate deriving (Eq, Show)
