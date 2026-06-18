module NetworkedComputation where
data MessageType = Request | Response | Event | Heartbeat | Vote | ReplicationUpdate | Acknowledgment deriving (Eq, Show)
