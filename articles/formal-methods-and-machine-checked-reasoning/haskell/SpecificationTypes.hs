module SpecificationTypes where
data VerificationStatus = Proved | Checked | Counterexample | Unknown deriving (Eq, Show)
data FormalEvidence = FormalEvidence { claim :: String, status :: VerificationStatus } deriving (Eq, Show)
