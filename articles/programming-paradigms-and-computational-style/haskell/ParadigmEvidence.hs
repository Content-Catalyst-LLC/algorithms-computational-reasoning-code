module ParadigmEvidence where

data Paradigm = Imperative | Procedural | Functional | ObjectOriented | Logic | Declarative | EventDriven deriving (Eq, Show)
data StyleEvidence = StyleEvidence { paradigm :: Paradigm, stateVisible :: Bool, testable :: Bool, traceable :: Bool } deriving (Eq, Show)
