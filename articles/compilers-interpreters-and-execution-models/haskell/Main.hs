module Main where

data Expr = Num Double | Add Expr Expr | Mul Expr Expr deriving (Eq, Show)

evalExpr :: Expr -> Double
evalExpr (Num x) = x
evalExpr (Add a b) = evalExpr a + evalExpr b
evalExpr (Mul a b) = evalExpr a * evalExpr b

main :: IO ()
main = do
  putStrLn "expression,result"
  putStrLn ("2 + 3 * 4," ++ show (evalExpr (Add (Num 2) (Mul (Num 3) (Num 4)))))
