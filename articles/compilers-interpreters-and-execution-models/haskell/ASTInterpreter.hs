module ASTInterpreter where
data Expr = Number Double | Plus Expr Expr | Times Expr Expr deriving (Eq, Show)
evaluate :: Expr -> Double
evaluate (Number x) = x
evaluate (Plus a b) = evaluate a + evaluate b
evaluate (Times a b) = evaluate a * evaluate b
