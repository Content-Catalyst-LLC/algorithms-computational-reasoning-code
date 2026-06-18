module Main where
window :: Int -> [a] -> [a]
window k xs = drop (max 0 (length xs - k)) xs
main :: IO ()
main = putStrLn ("test_name,value\nwindow_size,3\nlast_window," ++ show (window 3 ["A","B","A","C","D"]))
