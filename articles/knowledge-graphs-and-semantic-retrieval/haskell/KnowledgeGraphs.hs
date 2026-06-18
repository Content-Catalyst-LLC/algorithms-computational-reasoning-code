module KnowledgeGraphs where
data NodeType = Concept | Article | Reference | Repository | Dataset | Source deriving (Eq, Show)
data EdgeType = RelatedTo | Uses | Requires | Supports | Cites | Implements deriving (Eq, Show)
