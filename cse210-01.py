# Assignment: Wk 02 Ponder: Tic-Tac-Toe 
# Author: Melissa Howard

# main function of the game, when it runs the game is played
def main():
    squares = placeHolders()
    end = gameEnd(squares)
    player1Turn = False
    while end == "":
        player1Turn = not player1Turn
        grid(squares)
        playerMove(squares, player1Turn)
        end = gameEnd(squares)
    if end == "draw":
        print("it's a draw")
    elif player1Turn == True:
        print("Xs win")  
    else:
        print("Os win")  
    print("Good game! Thanks for playing")
    
    
#replaces placeholder with player marker
def playerMove(placeHolder, playerturn):
    playerName = "X"
    if playerturn == False:
        playerName = "O"
    pick = input(f"{playerName}'s turn to choose a square (1-9): ")
    while not (pick.isnumeric() and 1 <= int(pick) <= 9 and int(pick) in placeHolder):
        pick = input(f"{pick} is not a valid input. Please pick an available square: ")
    
    move = placeHolder.index(int(pick))
    placeHolder[move] = playerName
    return placeHolder

# initializes array of place holders for the squares that can be chosen
def placeHolders():
    placeHolders=[]
    for number in range(9):
        placeHolders.append(number + 1)
    return placeHolders

#outputs tic-tac-toe grid
def grid(placeHolders):
    print()
    print(placeHolders[0]," | ",placeHolders[1], " | ", placeHolders[2])
    print("---+-----+---")
    print(placeHolders[3]," | ",placeHolders[4], " | ", placeHolders[5])
    print("---+-----+---")
    print(placeHolders[6]," | ",placeHolders[7], " | ", placeHolders[8])

#initialize game end condition
def gameEnd(placeHolders):
    end = ""
    boardFilled = True
    for i in placeHolders:
        if isinstance(i, int):
            boardFilled = False

    if (placeHolders[0] == placeHolders[1] == placeHolders[2]):
       end = "win"
       return end
    elif (placeHolders[3] == placeHolders[4] == placeHolders[5]):
       end = "win"
       return end
    elif (placeHolders[6] == placeHolders[7] == placeHolders[8]):
       end = "win"
       return end
    elif (placeHolders[0] == placeHolders[3] == placeHolders[6]):
       end = "win"
       return end
    elif (placeHolders[1] == placeHolders[4] == placeHolders[7]):
       end = "win"
       return end
    elif (placeHolders[2] == placeHolders[5] == placeHolders[8]):
       end = "win"
       return end
    elif (placeHolders[0] == placeHolders[4] == placeHolders[8]):
       end = "win"
       return end
    elif (placeHolders[2] == placeHolders[4] == placeHolders[6]):
       end = "win"
       return end
    elif boardFilled:
        end = "draw"
        return end
    else:
        return end

#calls and runs main function
if __name__ == "__main__":
    main()