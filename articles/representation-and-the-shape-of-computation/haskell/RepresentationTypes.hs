module RepresentationTypes where
data Shape = ListShape | TableShape | TreeShape | GraphShape | VectorShape | StateShape deriving (Eq, Show)
data RepresentationEvidence = RepresentationEvidence { shape :: Shape, traceable :: Bool, governed :: Bool } deriving (Eq, Show)
