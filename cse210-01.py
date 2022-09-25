# Assignment: Wk 02 Ponder: Tic-Tac-Toe 
# Author: Melissa Howard

# main function of the game, when it runs the game is played
def main():
    squares = placeHolders()
    end = gameEnd(squares)
    player1Turn = True
    while end == "":
        grid(squares)
        playerMove(squares, player1Turn)
        end = gameEnd(squares)
        player1Turn = not player1Turn
    print("Game over")
    
#replaces placeholder with player marker
def playerMove(placeHolder, playerturn):
    pick = int(input("please choose a square (1-9): "))
    if pick in placeHolder:
        move = placeHolder.index(pick)
        if playerturn == True:
            placeHolder[move] = "X"
        else:
            placeHolder[move] = "O"
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