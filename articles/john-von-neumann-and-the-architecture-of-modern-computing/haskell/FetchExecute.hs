module Main where

step :: Int -> (String, Int) -> Int
step _ ("LOAD", x) = x
step acc ("ADD", x) = acc + x
step acc _ = acc

main :: IO ()
main = do
  let program = [("LOAD", 2), ("ADD", 3), ("STORE", 0), ("HALT", 0)]
  let acc = foldl step 0 program
  putStrLn ("accumulator=" ++ show acc)
