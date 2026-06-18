module StreamingAlgorithms where
data StreamingState = Counter | Sketch | Sample | Window deriving (Eq, Show)
