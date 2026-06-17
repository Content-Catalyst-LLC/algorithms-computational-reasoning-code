module ProvenanceTypes where

type Identifier = String
type Timestamp = String

data ProvenanceRelation = Used | WasGeneratedBy | WasDerivedFrom | WasAttributedTo deriving (Eq, Show)
data TraceEvent = TraceEvent { fromId :: Identifier, toId :: Identifier, relation :: ProvenanceRelation, timestamp :: Timestamp } deriving (Eq, Show)
