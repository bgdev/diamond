#!/usr/bin/env runhaskell

import Data.Char

diamond = map mirror . mirror . edge

dist a b = (ord a) - (ord b)

edge x = map (pad x) ['A' .. x]

mirror xs = xs ++ (tail $ reverse xs)

pad stop x = (spaces pre) ++ [x] ++ (spaces post)
  where len = dist stop 'A'
        post = dist x 'A'
        pre = len - post

spaces x = take x $ repeat ' '

main = mapM_ putStrLn $ diamond 'H'
