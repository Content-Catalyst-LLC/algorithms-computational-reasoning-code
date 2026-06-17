module AlgebraicDataTypes where

data Option a = None | Some a deriving (Eq, Show)
data Result a e = Ok a | Err e deriving (Eq, Show)
data ValidationError = MissingField String | InvalidSlug String | InvalidStatus String deriving (Eq, Show)
