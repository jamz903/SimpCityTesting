import pytest
play_menu = pytest.importorskip("play_menu")
from play_menu import *


def test_displayPlayMenu(monkeypatch, capsys):
    menu = "1. Build a HSE\n2. Build a BCH\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\n"
    monkeypatch.setattr('builtins.input', lambda _: "0")
    play_menu([],"HSE", "BCH",[["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]], 1)
    out, err = capsys.readouterr()
    assert out[0:len(menu)] == menu

#lower boundary
def test_LowerBoundaryInvalidOptionEntered(monkeypatch, capsys):
    menu = "1. Build a HSE\n2. Build a BCH\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\n"
    monkeypatch.setattr('builtins.input', lambda _: "-1")
    play_menu([],"HSE", "BCH",[["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]], 1)
    out, err = capsys.readouterr()
    assert out[len(menu):] == "Invalid option! Please try again!\n"

def test_Option0Selected(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "0")
    result = play_menu([],"HSE", "BCH",[["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]], 1)
    
    assert result == True

def test_Option1Selected(monkeypatch):
    menu = "1. Build a HSE\n2. Build a BCH\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\n"
    responses = iter(["1", "a1"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    option = play_menu([],"HSE", "BCH",[["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]], 1)
    assert option == "1"
    
# upper boundary
def test_Option4Selected(monkeypatch, capsys):
    menu = "1. Build a HSE\n2. Build a BCH\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\n"
    expectedOutput = "\nHSE: 0\nFAC: 0\nSHP: 0\nHWY: 0\nBCH: 0\nTotal score: 0\n"
    monkeypatch.setattr('builtins.input', lambda _: "4")
    play_menu([],"HSE", "BCH",[["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]], 1)
    out, err = capsys.readouterr()
    assert out[len(menu):] == expectedOutput

def test_Option5Selected(monkeypatch, capsys):
    menu = "1. Build a HSE\n2. Build a BCH\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\n"
    expectedOutput = "\nGame saved!\n"
    expectedBoard = [["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]]
    monkeypatch.setattr('builtins.input', lambda _: "5")
    play_menu([],"HSE", "BCH",[["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]], 1)

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

    out, err = capsys.readouterr()
    assert out[len(menu):] == expectedOutput and board == expectedBoard and turn_num == 1


def test_UpperBoundaryInvalidOptionEntered(monkeypatch, capsys):
    menu = "1. Build a HSE\n2. Build a BCH\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\n"
    monkeypatch.setattr('builtins.input', lambda _: "6")
    play_menu([],"HSE", "BCH",[["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]], 1)
    out, err = capsys.readouterr()
    assert out[len(menu):] == "Invalid option! Please try again!\n"
