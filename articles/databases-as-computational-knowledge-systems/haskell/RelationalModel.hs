module RelationalModel where
data Relation = Relation { relationName :: String, primaryKey :: String } deriving (Eq, Show)
