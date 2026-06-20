module GraphGovernance where
data GraphArtifact = GraphSpec | EdgeWeightRecord | ConstraintInventory | PathTrace | AlternativePathReport | UpdateLog deriving (Eq, Show)
