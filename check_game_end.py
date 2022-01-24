def check_game_end(board):
    counter = 0
    board_max = len(board) * len(board[0])
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            # checks if there is a building built
            if (board[i][j] != "?"):
                counter += 1

    if (counter == board_max):
        return True
    else:
        return False

#print(check_game_end([["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]]))
#print(check_game_end([["HSE","HSE","HSE","HSE"],["HSE","HSE","HSE","HSE"],["HSE","HSE","HSE","HSE"],["HSE","HSE","HSE","HSE"]]))
