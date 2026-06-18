module CloudModels where
data CloudLayer = Compute | Storage | Network | Data | Observability | Security | Governance deriving (Eq, Show)
