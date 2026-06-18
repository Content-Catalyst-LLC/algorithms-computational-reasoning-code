module SearchStrategy where
growth :: Int -> Int -> Int
growth b d = sum [b ^ level | level <- [0..d]]
