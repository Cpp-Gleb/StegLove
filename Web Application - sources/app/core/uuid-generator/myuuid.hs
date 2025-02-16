module Main where

import System.Environment (getArgs)
import UUIDList (nthUUID, uuidPosition)

main :: IO ()
main = do
    args <- getArgs
    case args of
      ["nth", nStr] ->
        case reads nStr of
          [(n, "")] -> do
              case nthUUID n of
                Just uuid -> putStrLn uuid
                Nothing   -> putStrLn "Index out of range"
          _ -> putStrLn "Incorrect number format (number must be integer)"

      ["pos", uuidStr] ->
        case uuidPosition uuidStr of
          Just n  -> print n
          Nothing -> putStrLn "Incorrect UUID."

      _ -> putStrLn "Usage: myuuid [nth <index> | pos <UUID>]"
