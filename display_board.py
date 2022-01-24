# function to display the board to user
# takes in the turn number, and the board to display
def display_board(turn_num, board):
    if (turn_num == None):
        print("\nFinal layout of Simp City:")
    else: 
        print("\nTurn " + str(turn_num))
    
    print("     A     B     C     D   ")
    print("  +-----+-----+-----+-----+")
    for i in range(len(board)):
        print(" " + str(i+1) + "|", end = "")
        for j in range(len(board[i])):
            if (board[i][j] != "?"):
                print(" " + board[i][j] + " |", end = "")
            else:
                print("     |", end = "")
        print("\n  +-----+-----+-----+-----+")
    return

#display_board(None, [["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]])