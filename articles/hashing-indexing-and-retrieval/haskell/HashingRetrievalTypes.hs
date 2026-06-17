module HashingRetrievalTypes where

type Key = String
type Value = String
data RetrievalStructure = HashMap | DatabaseIndex | InvertedIndex | Cache | ContentAddressedStore deriving (Eq, Show)
data RetrievalEvidence = RetrievalEvidence { key :: Key, value :: Value, source :: String, version :: Int } deriving (Eq, Show)
