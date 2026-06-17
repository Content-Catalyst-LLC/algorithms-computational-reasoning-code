module GraphTypes where

type Node = String
type Edge = (Node, Node)
type WeightedEdge = (Node, Node, Double)

data Graph = Graph [Node] [Edge] deriving (Eq, Show)
data WeightedGraph = WeightedGraph [Node] [WeightedEdge] deriving (Eq, Show)
