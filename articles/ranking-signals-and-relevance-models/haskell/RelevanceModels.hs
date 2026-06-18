module RelevanceModels where
data RelevanceModel = RuleBased | VectorSpace | BM25 | LearningToRank | NeuralReranker | Hybrid deriving (Eq, Show)
