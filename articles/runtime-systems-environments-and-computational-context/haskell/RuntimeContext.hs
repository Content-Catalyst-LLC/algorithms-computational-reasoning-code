module RuntimeContext where
data RuntimeContext = RuntimeContext { runtime :: String, platform :: String, dependencies :: [String] } deriving (Eq, Show)
