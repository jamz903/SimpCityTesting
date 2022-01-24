import pytest
load_saved_game = pytest.importorskip("load_saved_game")
from load_saved_game import *

def test_Load_Saved_Game_fileDoesNotExist(capsys):
    result = load_saved_game("test.csv")
    out, err = capsys.readouterr()
    assert out == "No saved game file found! Starting new game...\n"


def test_Load_Saved_Game_fileDoesExist():
    file = open("SimpCityBoard.csv", "w")
    file.write("3\n")
    board = [["HSE", "?", "?", "?"], 
             ["?", "?", "?", "?"], 
             ["?", "?", "BCH", "?"], 
             ["?", "?", "?", "?"]]
    for i in range(len(board)):
        for j in range(len(board[i])):
            file.write(board[i][j])
            if j != (len(board[i])-1):
                file.write(",")
        file.write("\n")
    file.close()
    result = load_saved_game("SimpCityBoard.csv")
    assert result == {
        'turn_num': 3,
        'saved_game': [['HSE', '?', '?', '?'],
                       ['?', '?', '?', '?'],
                       ['?', '?', 'BCH', '?'],
                       ['?', '?', '?', '?']]
    }


