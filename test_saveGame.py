import pytest
save_game = pytest.importorskip("save_game")
from save_game import *

def test_saveGame(capsys):
    save_game(3, [["?","HSE","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","BCH"]])
    out, err = capsys.readouterr()
    expectedOutput = "Game saved!\n"

    board = []
    count = 0
    turn_num = 0
    # loops through each line in the .csv file
    for i in open("SimpCityBoard.csv"):
        i = i.strip("\n")

        # checks if the current line is first line
        # if is first line, retrieve the turn number, stored in the first line of the .csv file
        if count == 0:
            turn_num = int(i)
            count += 1
            continue
        # if not first line, split the line by ',' and append it to the board
        row = i.split(",")
        board.append(row)
    
    assert turn_num == 3 and board == [["?","HSE","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","BCH"]] and out == expectedOutput