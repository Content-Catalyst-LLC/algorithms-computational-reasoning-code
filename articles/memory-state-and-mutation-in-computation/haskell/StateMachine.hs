module StateMachine where
data Status = Draft | Review | Published | Archived deriving (Eq, Show)
