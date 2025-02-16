{-# LANGUAGE BangPatterns #-}
module FeistelPermutation
  ( feistelForward
  , feistelInverse
  ) where

import Data.Bits (xor, shiftL, shiftR, (.|.), (.&.))

roundKeys :: [Integer]
roundKeys =
  [ 0x0123456789ABCDEF
  , 0xFEDCBA9876543210
  , 0xA5A5A5A5A5A5A5A5
  , 0x5A5A5A5A5A5A5A5A
  , 0x1111111111111111
  , 0x2222222222222222
  , 0x3333333333333333
  , 0x4444444444444444
  ]

numRounds :: Int
numRounds = length roundKeys

feistelForward :: Integer -> Integer
feistelForward n =
  let (l0, r0) = split122 n
      (lf, rf) = foldl feistelEncRound (l0, r0) (zip [0..] roundKeys)
  in join122 (lf, rf)

feistelInverse :: Integer -> Integer
feistelInverse x =
  let (l0, r0) = split122 x
      (lf, rf) = foldr feistelDecRound (l0, r0) (zip [0..] roundKeys)
  in join122 (lf, rf)

split122 :: Integer -> (Integer, Integer)
split122 x =
  let mask61 = (1 `shiftL` 61) - 1 
      !l     = x .&. mask61
      !r     = x `shiftR` 61
  in (l, r)

join122 :: (Integer, Integer) -> Integer
join122 (l, r) =
  let shiftAmt = 61
  in (r `shiftL` shiftAmt) .|. (l .&. ((1 `shiftL` shiftAmt) - 1))

feistelEncRound :: (Integer, Integer) -> (Int, Integer) -> (Integer, Integer)
feistelEncRound (l, r) (i, key) =
  let newL = r
      newR = l `xor` roundFunction r i key
  in (newL, newR)

feistelDecRound :: (Int, Integer) -> (Integer, Integer) -> (Integer, Integer)
feistelDecRound (i, key) (l, r) =
  let oldR = l
      oldL = r `xor` roundFunction l i key
  in (oldL, oldR)

roundFunction :: Integer -> Int -> Integer -> Integer
roundFunction r i key =
  let modBase = (1 `shiftL` 61)
      tmp1  = (r + key + fromIntegral i) `mod` modBase
      rot13 = rotateLeft tmp1 13 61
      out   = (rot13 `xor` (key `shiftR` 3)) `mod` modBase
  in out

rotateLeft :: Integer -> Int -> Int -> Integer
rotateLeft x s width =
  let msb = (1 `shiftL` width) - 1
      s'  = s `mod` width
      left  = (x `shiftL` s') .&. msb
      right = x `shiftR` (width - s')
  in (left .|. right) .&. msb

