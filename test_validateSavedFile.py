import pytest
import csv
validate_saved_file = pytest.importorskip("validate_saved_file")
save_game = pytest.importorskip("save_game")
from validate_saved_file import *
from save_game import *

def test_validateSavedFile_emptyBoard():
    board = [["?", "?", "?", "?"], 
             ["?", "?", "?", "?"], 
             ["?", "?", "?", "?"], 
             ["?", "?", "?", "?"]]
    save_game(1, board)

    result = validate_saved_file("SimpCityBoard.csv")
    assert result == True

def test_validateSavedFile_invalidBuildingTypes():
    board = [["?", "?", "?", "?"], 
             ["?", "SGP", "CHN", "?"], 
             ["?", "?", "HKG", "?"], 
             ["?", "?", "?", "?"]]
    save_game(4, board)

    result = validate_saved_file("SimpCityBoard.csv")
    assert result == False

def test_validateSavedFile_additionalContentAtLastLine():
    board = [["?", "?", "?", "?"], 
             ["?", "HSE", "FAC", "?"], 
             ["?", "?", "SHP", "?"], 
             ["?", "?", "?", "?"]]
    save_game(7, board)
    with open('SimpCityBoard.csv','a') as fd:
        fd.write("\ntest,test2,test3")
    
    result = validate_saved_file("SimpCityBoard.csv")
    assert result == False

def test_validateSavedFile_turnNumMatchBuildingsPlaced_Pass():
    board = [["?", "?", "?", "?"], 
             ["?", "HSE", "FAC", "?"], 
             ["?", "?", "SHP", "?"], 
             ["?", "?", "?", "?"]]
    save_game(4, board)

    result = validate_saved_file("SimpCityBoard.csv")
    expectedResult = True
    assert result == expectedResult

def test_validateSavedFile_turnNumMatchBuildingsPlaced_Fail():
    board = [["?", "?", "?", "?"], 
             ["?", "HSE", "FAC", "?"], 
             ["?", "?", "SHP", "?"], 
             ["?", "?", "?", "?"]]
    save_game(99, board)

    result = validate_saved_file("SimpCityBoard.csv")
    expectedResult = False
    assert result == expectedResult
    
def test_validateSavedFile_validBuildingPlacement_Case1():
    board = [["?", "?", "?", "?"], 
             ["?", "?", "FAC", "?"], 
             ["?", "?", "?", "?"], 
             ["?", "?", "?", "?"]]
    save_game(2, board)

    result = validate_saved_file("SimpCityBoard.csv")
    expectedResult = True
    assert result == expectedResult

def test_validateSavedFile_validBuildingPlacement_Case2():
    board = [["?", "?", "?", "?"], 
             ["?", "?", "FAC", "?"], 
             ["?", "HSE", "HWY", "?"], 
             ["?", "?", "SHP", "?"]]
    save_game(5, board)

    result = validate_saved_file("SimpCityBoard.csv")
    expectedResult = True
    assert result == expectedResult

def test_validateSavedFile_invalidBuildingPlacement():
    board = [["?", "?", "?", "?"], 
             ["?", "?", "FAC", "?"], 
             ["?", "?", "?", "?"], 
             ["HWY", "?", "?", "?"]]
    save_game(3, board)

    result = validate_saved_file("SimpCityBoard.csv")
    expectedResult = False
    assert result == expectedResult

# Each building type cannot exceed 8
# This test case has 10 FAC on the board
def test_validateSavedFile_invalidBuildingOccurrence():
    board = [["FAC", "FAC", "FAC", "FAC"], 
             ["?", "?", "FAC", "FAC"], 
             ["FAC", "FAC", "FAC", "FAC"], 
             ["HWY", "?", "?", "?"]]
    save_game(11, board)

    result = validate_saved_file("SimpCityBoard.csv")
    expectedResult = False
    assert result == expectedResult