module EmbeddedGovernance where
data EmbeddedControl = SensorValidation | DeadlineCheck | FailSafeMode | SignedUpdate | FieldDiagnostics | DataMinimization deriving (Eq, Show)
