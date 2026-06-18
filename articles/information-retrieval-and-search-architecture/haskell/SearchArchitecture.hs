module SearchArchitecture where
data SearchLayer = Collection | Index | QueryProcessing | Ranking | Evaluation | Governance deriving (Eq, Show)
