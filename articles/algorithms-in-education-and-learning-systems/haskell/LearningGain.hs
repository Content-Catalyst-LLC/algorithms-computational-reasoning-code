module Main where

main :: IO ()
main = do
  let pretest = 0.52
      posttest = 0.78
      gain = posttest - pretest
  putStrLn ("learning_gain=" ++ show gain)
