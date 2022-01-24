import pytest
display_board = pytest.importorskip("display_board")
from display_board import *

def test_displayBoard_withTurnNum(capsys):
    expected_result = "\nTurn 3\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1|     |     |     |     |\n  +-----+-----+-----+-----+\n 2|     |     |     |     |\n  +-----+-----+-----+-----+\n 3|     |     |     |     |\n  +-----+-----+-----+-----+\n 4|     |     |     |     |\n  +-----+-----+-----+-----+\n"
    display_board(3, [["?", "?", "?", "?"], ["?", "?", "?", "?"],
              ["?", "?", "?", "?"], ["?", "?", "?", "?"]])
    out, err = capsys.readouterr()
    assert out == expected_result
   
def test_displayBoard_withoutTurnNum(capsys):
    expected_result = "\nFinal layout of Simp City:\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1|     |     |     |     |\n  +-----+-----+-----+-----+\n 2|     |     |     |     |\n  +-----+-----+-----+-----+\n 3|     |     |     |     |\n  +-----+-----+-----+-----+\n 4|     |     |     |     |\n  +-----+-----+-----+-----+\n"
    display_board(None, [["?", "?", "?", "?"], ["?", "?", "?", "?"],
              ["?", "?", "?", "?"], ["?", "?", "?", "?"]])
    out, err = capsys.readouterr()
    assert out == expected_result