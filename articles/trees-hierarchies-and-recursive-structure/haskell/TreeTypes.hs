module TreeTypes where
data Tree a = Leaf a | Branch a [Tree a] deriving (Eq, Show)

height :: Tree a -> Int
height (Leaf _) = 0
height (Branch _ children) = 1 + maximum (0 : map height children)
