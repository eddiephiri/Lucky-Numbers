####**************************** LUCKY NUMBERS *********************************
#   Program simulates the lucky number game
#   This is a game were there are a total of 48 balls.
#   You are to pick six (6) numbers from this range
#   The computer will pick a total number of 35 numbers from the total number at random
#   You win by matching all your six numbers with those picked by the computer
#   Your ticket fails if you pick one not chosen by the random picker




if __name__ == '__main__':
    from modules.Numgenerator import draw
    from modules.Gentickets import generate as gen
    from modules.Checktickets import check
    from modules.Display import results 
else:
    print("Imported as a module!")
    
