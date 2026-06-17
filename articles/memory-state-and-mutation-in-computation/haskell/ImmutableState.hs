module ImmutableState where
data Article = Article { title :: String, status :: String } deriving (Eq, Show)
