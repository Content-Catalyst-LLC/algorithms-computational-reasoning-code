-- Conceptual Haskell note: Monte Carlo workflows are typed as sampled inputs, model evaluation, and summary statistics.
module MonteCarloNote where

data Trial a b = Trial { sampledInput :: a, modelOutput :: b }

data Summary = Summary { estimate :: Double, standardError :: Double, lower95 :: Double, upper95 :: Double }
