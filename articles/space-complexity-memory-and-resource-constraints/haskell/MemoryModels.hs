module MemoryModels where
totalSpace :: Integer -> Integer -> Integer -> Integer
totalSpace input output auxiliary = input + output + auxiliary
