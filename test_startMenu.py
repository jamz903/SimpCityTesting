import pytest
start_menu = pytest.importorskip("start_menu")
from start_menu import *

def test_displayStartMenu(monkeypatch, capsys):
    output="Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit\n"
    monkeypatch.setattr('builtins.input', lambda _: "0")
    start_menu(i=2)
    out, err = capsys.readouterr()
    assert out[0:len(output)] == output

def test_startMenuLowerBoundaryA(monkeypatch, capsys):
    output="Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit\n"
    monkeypatch.setattr('builtins.input', lambda _: "-1")
    start_menu(i=1)
    out, err = capsys.readouterr()
    assert out[len(output):] == "Invalid option! Please try again!\n\n"


def test_startMenuLowerBoundaryB(monkeypatch, capsys):
    output="Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit\n"
    monkeypatch.setattr('builtins.input', lambda _: "0")
    start_menu(i=1)
    out, err = capsys.readouterr()
    assert out[len(output):] == "Exiting Simp City...\n"

def test_startMenuLowerBoundaryC(monkeypatch, capsys):
    output="Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit\n"
    responses = iter(['1', "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    start_menu(i=1)
    out, err = capsys.readouterr()
    assert "\nTurn 1\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1|     |     |     |     |\n  +-----+-----+-----+-----+\n 2|     |     |     |     |\n  +-----+-----+-----+-----+\n 3|     |     |     |     |\n  +-----+-----+-----+-----+\n 4|     |     |     |     |\n  +-----+-----+-----+-----+\n" in out[len(output):]


def test_startMenuUpperBoundaryA(monkeypatch, capsys):
    output="Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit\n"
    responses = iter(['1', "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    start_menu(i=1)
    out, err = capsys.readouterr()
    assert "\nTurn 1\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1|     |     |     |     |\n  +-----+-----+-----+-----+\n 2|     |     |     |     |\n  +-----+-----+-----+-----+\n 3|     |     |     |     |\n  +-----+-----+-----+-----+\n 4|     |     |     |     |\n  +-----+-----+-----+-----+\n" in out[len(output):]

def test_startMenuUpperBoundaryBSavedGameFileExists(monkeypatch, capsys):
    output="Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit\n"
    responses = iter(['2', "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
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
    start_menu(i=1)
    out, err = capsys.readouterr()
    assert "\nTurn 3\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1| HSE | BCH |     |     |\n  +-----+-----+-----+-----+\n 2|     |     |     |     |\n  +-----+-----+-----+-----+\n 3|     |     |     |     |\n  +-----+-----+-----+-----+\n 4|     |     |     |     |\n  +-----+-----+-----+-----+\n" in out

def test_startMenuUpperBoundaryBSavedGameFileDoesNotExists(monkeypatch, capsys):
    output="Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit\n"
    responses = iter(['2', "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    filename = "SimpCityBoard.csv"
    if (os.path.exists(filename)):
        os.remove(filename)
    start_menu(i=1)
    out, err = capsys.readouterr()
    assert "\nTurn 1\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1|     |     |     |     |\n  +-----+-----+-----+-----+\n 2|     |     |     |     |\n  +-----+-----+-----+-----+\n 3|     |     |     |     |\n  +-----+-----+-----+-----+\n 4|     |     |     |     |\n  +-----+-----+-----+-----+\n" in out
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


def test_startMenuUpperBoundaryC(monkeypatch, capsys):
    output="Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit\n"
    monkeypatch.setattr('builtins.input', lambda _: "3")
    start_menu(i=1)
    out, err = capsys.readouterr()
    assert out[len(output):] == "Invalid option! Please try again!\n\n"
