module ModularBoundary where
data Boundary = Boundary { provider :: String, consumer :: String, contract :: String } deriving (Eq, Show)
