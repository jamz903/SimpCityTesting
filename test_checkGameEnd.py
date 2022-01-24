import pytest
check_game_end = pytest.importorskip("check_game_end")
from check_game_end import *

def test_checkGameEnd_GameEnded():
    expectedOutput = True
    result = check_game_end([["HSE","HSE","HSE","HSE"],["HSE","HSE","HSE","HSE"],["HSE","HSE","HSE","HSE"],["HSE","HSE","HSE","HSE"]])
    assert expectedOutput == result

def test_checkGameEnd_GameHasNotEndEmptyBoard():
    expectedOutput = False
    result = check_game_end([["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]])
    assert expectedOutput == result

def test_checkGameEnd_GameHasNotEndNonEmptyBoard():
    expectedOutput = False
    result = check_game_end([["HSE","HSE","HSE","HSE"],["HSE","HSE","HSE","HSE"],["HSE","HSE","HSE","?"],["HSE","HSE","HSE","HSE"]])
    assert expectedOutput == result