# Assignment: Wk 02 Ponder: Tic-Tac-Toe 
# Author: Melissa Howard

# main function of the game, when it runs the game is played
def main():
    squares = placeHolders()
    #print(squares)
    grid(squares)

# initializes array of place holders for the squares that can be chosen
def placeHolders():
    placeHolders=[]
    for number in range(9):
        placeHolders.append(number + 1)
    return placeHolders

#initalizes tic-tac-toe grid
def grid(placeHolders):
    print()
    print(placeHolders[0]," | ",placeHolders[1], " | ", placeHolders[2])
    print("---+-----+---")
    print(placeHolders[3]," | ",placeHolders[4], " | ", placeHolders[5])
    print("---+-----+---")
    print(placeHolders[6]," | ",placeHolders[7], " | ", placeHolders[8])

#calls and runs main function
if __name__ == "__main__":
    main()