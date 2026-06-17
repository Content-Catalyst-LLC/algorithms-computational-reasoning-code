module ArchitectureGraph where
type Component = String
type Edge = (Component, Component)
dependencyCount :: [Edge] -> Int
dependencyCount = length
