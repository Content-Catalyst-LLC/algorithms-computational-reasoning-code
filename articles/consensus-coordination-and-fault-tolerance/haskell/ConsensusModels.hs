module ConsensusModels where
data ConsensusProperty = Agreement | Validity | Integrity | Termination | Ordering | Durability deriving (Eq, Show)
