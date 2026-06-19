module EdgeModels where
data EdgeLayer = Device | Gateway | LocalServer | NetworkEdge | CloudCore deriving (Eq, Show)
