module SequenceStructureTypes where
data SequenceShape = ArrayShape | ListShape | StackShape | QueueShape | DequeShape | CircularBufferShape deriving (Eq, Show)
data StructureEvidence = StructureEvidence { shape :: SequenceShape, invariantDocumented :: Bool, overflowPolicy :: Bool } deriving (Eq, Show)
