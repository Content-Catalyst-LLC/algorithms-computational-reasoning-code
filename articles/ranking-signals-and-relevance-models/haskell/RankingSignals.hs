module RankingSignals where
data RankingSignal = Lexical | FieldWeight | Metadata | Freshness | Authority | Semantic | Feedback | Provenance deriving (Eq, Show)
