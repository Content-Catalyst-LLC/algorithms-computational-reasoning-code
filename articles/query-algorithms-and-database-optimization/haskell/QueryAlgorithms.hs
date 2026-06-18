module QueryAlgorithms where
data JoinAlgorithm = NestedLoop | IndexNestedLoop | HashJoin | MergeJoin | BroadcastJoin | ShuffleJoin deriving (Eq, Show)
