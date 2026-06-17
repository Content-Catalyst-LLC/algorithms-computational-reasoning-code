module LambdaTerms where
data Term = Var String | Lam String Term | App Term Term deriving (Eq, Show)
identity :: Term
identity = Lam "x" (Var "x")
