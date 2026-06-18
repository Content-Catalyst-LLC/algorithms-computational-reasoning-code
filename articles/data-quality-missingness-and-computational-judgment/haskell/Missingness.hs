module Missingness where
data MissingnessReason = Unknown | NotApplicable | NotCollected | Withheld | Pending | Invalid | Redacted | StructuralZero deriving (Eq, Show)
