module ConstraintModels where
data ConstraintType = HardConstraint | SoftConstraint | Equality | Inequality | Compatibility deriving (Eq, Show)
data Feasibility = Feasible | Infeasible | Unsatisfiable deriving (Eq, Show)
