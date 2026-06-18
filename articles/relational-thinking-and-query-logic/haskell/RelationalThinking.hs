module RelationalThinking where
data RelationalOperation = Selection | Projection | Join | AntiJoin | Aggregation | RecursiveQuery deriving (Eq, Show)
