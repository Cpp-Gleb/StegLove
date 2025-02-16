{-# LANGUAGE OverloadedStrings #-}

module UUIDList
    ( nthUUID
    , uuidPosition
    ) where

import Data.Bits (shiftL, shiftR, (.|.), (.&.), xor)
import Data.Char (digitToInt, toLower)
import Text.Printf (printf)

import FeistelPermutation (feistelForward, feistelInverse)

nthUUID :: Integer -> Maybe String
nthUUID n
  | n < 0 || n >= (2^(122 :: Integer)) = Nothing
  | otherwise = 
      let x     = feistelForward n  
          val   = embedBits x
          uuid  = formatUuid val
      in Just uuid

uuidPosition :: String -> Maybe Integer
uuidPosition str = do
  val128 <- uuidStringToInteger str
  x122   <- extractBits val128
  let n  = feistelInverse x122
  return n

embedBits :: Integer -> Integer
embedBits x =
  let
    timeLow    =  x .&. 0xFFFFFFFF
    timeMid    = (x `shiftR` 32)  .&. 0xFFFF
    timeHi     = (x `shiftR` 48)  .&. 0xFFF    
    clockSeq   = (x `shiftR` 60)  .&. 0x3FFF    
    node       = (x `shiftR` 74)  .&. 0xFFFFFFFFFFFF 

    versioned  = (4 `shiftL` 12) .|. timeHi 
    variantSeq = (2 `shiftL` 14) .|. clockSeq  

    val =  (timeLow   `shiftL` 96)
       .|. (timeMid   `shiftL` 80)
       .|. (versioned `shiftL` 64)
       .|. (variantSeq `shiftL` 48)
       .|. node
  in val

extractBits :: Integer -> Maybe Integer
extractBits uuidVal =
  let versionNibble = (uuidVal `shiftR` 76) .&. 0xF
  in if versionNibble /= 4
       then Nothing
       else 
         let variantBits = (uuidVal `shiftR` 62) .&. 0x3
         in if variantBits /= 2
              then Nothing
              else Just (extract122 uuidVal)

extract122 :: Integer -> Integer
extract122 u =
  let
    timeLow    = (u `shiftR` 96) .&. 0xFFFFFFFF
    timeMid    = (u `shiftR` 80) .&. 0xFFFF
    vers       = (u `shiftR` 64) .&. 0xFFFF   
    timeHi     = vers .&. 0xFFF
    varSeq     = (u `shiftR` 48) .&. 0xFFFF   
    clockSeq   = varSeq .&. 0x3FFF
    node       = u .&. 0xFFFFFFFFFFFF

    x =  timeLow
     .|. (timeMid `shiftL` 32)
     .|. (timeHi  `shiftL` 48)
     .|. (clockSeq `shiftL` 60)
     .|. (node `shiftL` 74)
  in x

toHex :: Integer -> String
toHex val = printf "%032x" val

formatUuid :: Integer -> String
formatUuid val =
  let h = toHex val
  in  take 8 h ++ "-" ++
      take 4 (drop 8 h)  ++ "-" ++
      take 4 (drop 12 h) ++ "-" ++
      take 4 (drop 16 h) ++ "-" ++
      drop 20 h

uuidStringToInteger :: String -> Maybe Integer
uuidStringToInteger raw =
  let filtered = filter (/= '-') raw
  in if length filtered /= 32
       then Nothing
       else fromHex filtered

fromHex :: String -> Maybe Integer
fromHex = go 0
  where
    go acc [] = Just acc
    go acc (c:cs) =
      let c' = toLower c
      in if (c' >= '0' && c' <= '9') || (c' >= 'a' && c' <= 'f')
           then go (acc*16 + toInteger (digitToInt c')) cs
           else Nothing

