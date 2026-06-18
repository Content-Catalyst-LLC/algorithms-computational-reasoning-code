module DatabaseKnowledge where
data KnowledgeLayer = Schema | Constraint | Query | Metadata | Provenance | Governance deriving (Eq, Show)
