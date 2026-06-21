module Main where
main :: IO ()
main = do
  let alpha = 2.0 :: Double; beta = 2.0 :: Double; successes = 113.0 :: Double; failures = 72.0 :: Double
      postAlpha = alpha + successes; postBeta = beta + failures
  putStrLn ("posterior_mean=" ++ show (postAlpha / (postAlpha + postBeta)))
