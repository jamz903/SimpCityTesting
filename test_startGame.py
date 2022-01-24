import builtins
import pytest
start_game = pytest.importorskip("start_game")
from start_game import *
import os

def test_startNewGame(capsys, monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "0")
    start_game()
    out, err = capsys.readouterr()

    expectedBoardResult = "\nTurn 1\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1|     |     |     |     |\n  +-----+-----+-----+-----+\n 2|     |     |     |     |\n  +-----+-----+-----+-----+\n 3|     |     |     |     |\n  +-----+-----+-----+-----+\n 4|     |     |     |     |\n  +-----+-----+-----+-----+\n"
    
    assert out[0:len(expectedBoardResult)] == expectedBoardResult

def test_startLoadSavedGame_SavedFileExistsButInvalidSavedFile(capsys, monkeypatch):
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
    monkeypatch.setattr("builtins.input", lambda _: "0")
    start_game(True)
    out, err = capsys.readouterr()

    # expectedBoardResult = "\nTurn 3\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1| HSE |     |     |     |\n  +-----+-----+-----+-----+\n 2|     |     |     |     |\n  +-----+-----+-----+-----+\n 3|     |     | BCH |     |\n  +-----+-----+-----+-----+\n 4|     |     |     |     |\n  +-----+-----+-----+-----+\n"
    expectedOutput = "The saved file is invalid. Returning to main menu.\n"

    assert out[0:len(expectedOutput)] == expectedOutput

def test_startLoadSavedGame_SavedFileExistsAndValidSavedFile(capsys, monkeypatch):
    file = open("SimpCityBoard.csv", "w")
    file.write("3\n")
    board = [["HSE", "BCH", "?", "?"], 
             ["?", "?", "?", "?"], 
             ["?", "?", "?", "?"], 
             ["?", "?", "?", "?"]]
    for i in range(len(board)):
        for j in range(len(board[i])):
            file.write(board[i][j])
            if j != (len(board[i])-1):
                file.write(",")
        file.write("\n")
    file.close()
    monkeypatch.setattr("builtins.input", lambda _: "0")
    start_game(True)
    out, err = capsys.readouterr()

    expectedBoardResult = "\nTurn 3\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1| HSE | BCH |     |     |\n  +-----+-----+-----+-----+\n 2|     |     |     |     |\n  +-----+-----+-----+-----+\n 3|     |     |     |     |\n  +-----+-----+-----+-----+\n 4|     |     |     |     |\n  +-----+-----+-----+-----+\n"

    assert out[0:len(expectedBoardResult)] == expectedBoardResult

def test_startLoadSavedGameSavedFileDoesNotExists(capsys, monkeypatch):
    filename = "SimpCityBoard.csv"
    if (os.path.exists(filename)):
        os.remove(filename)
    monkeypatch.setattr("builtins.input", lambda _: "0")
    start_game(True)
    out, err = capsys.readouterr()

    expectedBoardResult = "No saved game file found! Starting new game...\n\n\nTurn 1\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1|     |     |     |     |\n  +-----+-----+-----+-----+\n 2|     |     |     |     |\n  +-----+-----+-----+-----+\n 3|     |     |     |     |\n  +-----+-----+-----+-----+\n 4|     |     |     |     |\n  +-----+-----+-----+-----+\n"
    
    assert out[0:len(expectedBoardResult)] == expectedBoardResult
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

def test_startGame_gameEnds(capsys, monkeypatch):
    file = open("SimpCityBoard.csv", "w")
    file.write("16\n")
    board = [["HSE", "HSE", "HSE", "HSE"], 
             ["FAC", "FAC", "FAC", "FAC"], 
             ["BCH", "BCH", "BCH", "BCH"], 
             ["HWY", "HWY", "HWY", "?"]]
    for i in range(len(board)):
        for j in range(len(board[i])):
            file.write(board[i][j])
            if j != (len(board[i])-1):
                file.write(",")
        file.write("\n")
    file.close()
    responses = iter(["1", "d4", "0"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    start_game(True)
    out, err = capsys.readouterr()
    expectedOutput_BCH = "\nFinal layout of Simp City:\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1| HSE | HSE | HSE | HSE |\n  +-----+-----+-----+-----+\n 2| FAC | FAC | FAC | FAC |\n  +-----+-----+-----+-----+\n 3| BCH | BCH | BCH | BCH |\n  +-----+-----+-----+-----+\n 4| HWY | HWY | HWY | BCH |\n  +-----+-----+-----+-----+\n"
    expectedOutput_HSE = "\nFinal layout of Simp City:\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1| HSE | HSE | HSE | HSE |\n  +-----+-----+-----+-----+\n 2| FAC | FAC | FAC | FAC |\n  +-----+-----+-----+-----+\n 3| BCH | BCH | BCH | BCH |\n  +-----+-----+-----+-----+\n 4| HWY | HWY | HWY | HSE |\n  +-----+-----+-----+-----+\n"
    expectedOutput_HWY = "\nFinal layout of Simp City:\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1| HSE | HSE | HSE | HSE |\n  +-----+-----+-----+-----+\n 2| FAC | FAC | FAC | FAC |\n  +-----+-----+-----+-----+\n 3| BCH | BCH | BCH | BCH |\n  +-----+-----+-----+-----+\n 4| HWY | HWY | HWY | HWY |\n  +-----+-----+-----+-----+\n"
    expectedOutput_SHP = "\nFinal layout of Simp City:\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1| HSE | HSE | HSE | HSE |\n  +-----+-----+-----+-----+\n 2| FAC | FAC | FAC | FAC |\n  +-----+-----+-----+-----+\n 3| BCH | BCH | BCH | BCH |\n  +-----+-----+-----+-----+\n 4| HWY | HWY | HWY | SHP |\n  +-----+-----+-----+-----+\n"
    expectedOutput_FAC = "\nFinal layout of Simp City:\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1| HSE | HSE | HSE | HSE |\n  +-----+-----+-----+-----+\n 2| FAC | FAC | FAC | FAC |\n  +-----+-----+-----+-----+\n 3| BCH | BCH | BCH | BCH |\n  +-----+-----+-----+-----+\n 4| HWY | HWY | HWY | FAC |\n  +-----+-----+-----+-----+\n"
    assert expectedOutput_BCH in out or expectedOutput_HSE in out or expectedOutput_HWY in out or expectedOutput_SHP in out or expectedOutput_FAC in out
