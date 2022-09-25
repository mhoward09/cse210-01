# Assignment: Wk 02 Ponder: Tic-Tac-Toe 
# Author: Melissa Howard

# main function of the game, when it runs the game is played
def main():
    squares = placeHolders()
    print(squares)

# initializes array of place holders for the squares that can be chosen
def placeHolders():
    placeHolders=[]
    for number in range(9):
        placeHolders.append(number + 1)
    return placeHolders

if __name__ == "__main__":
    main()