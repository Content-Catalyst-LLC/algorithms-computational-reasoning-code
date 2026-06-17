module DataStructureTypes where
data StructureShape = Array | List | Stack | Queue | Set | Map | Tree | Heap | Graph | Table | Vector deriving (Eq, Show)
data StructureEvidence = StructureEvidence { shape :: StructureShape, invariantDocumented :: Bool, governed :: Bool } deriving (Eq, Show)
