module Main where

main :: IO ()
main = do
  let rates = [0.42, 0.31, 0.36]
      selectionGap = maximum rates - minimum rates
  putStrLn ("selection_gap=" ++ show selectionGap)
