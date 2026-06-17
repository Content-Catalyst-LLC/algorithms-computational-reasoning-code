module InterfaceContract where
data Contract = Contract { name :: String, version :: String, requiredFields :: [String] } deriving (Eq, Show)
