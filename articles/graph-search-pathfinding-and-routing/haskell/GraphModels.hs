module GraphModels where
data GraphKind = Directed | Undirected | Weighted | Labeled deriving (Eq, Show)
data Traversal = BreadthFirst | DepthFirst | Dijkstra | HeuristicPathfinding deriving (Eq, Show)
