module QueueingModels where
data QueueControl = Backpressure | LoadShedding | RateLimit | CircuitBreaker | RetryWithJitter deriving (Eq, Show)
