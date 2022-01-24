from place_building import *
import pytest

def test_placeBuildingPassed():

    board = [["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]]
    result = place_building("HSE", "a1", board)
    assert board == [["HSE", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]] and result == True

def test_placeBuildingOrthogonallyAdjacentToExistingBuildingHorizontal():
    board = [["?", "BCH", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]]
    result = place_building("HSE", "a1", board)
    assert board == [["HSE", "BCH", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]] and result == True

def test_placeBuildingOrthogonallyAdjacentToExistingBuildingVertical():
    board = [["?", "BCH", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]]
    result = place_building("HSE", "b2", board)
    assert board == [["?", "BCH", "?", "?"], ["?", "HSE", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]] and result == True

def test_placeBuildingMissingBoardCoordinate(capsys):
    board = [["?", "BCH", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]]
    result = place_building("HSE", "", board)
    out, err = capsys.readouterr()
    expectedMessage = "Invalid input! Please enter in a valid location coordinate!\n"
    assert result == False and out[0:len(expectedMessage)] == expectedMessage

def test_placeBuildingInvalidBoardCoordinateLength(capsys):
    board = [["?", "BCH", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]]
    result = place_building("HSE", "a11", board)
    out, err = capsys.readouterr()
    expectedMessage = "Invalid input! Please enter in a valid location coordinate!\n"
    assert result == False and out[0:len(expectedMessage)] == expectedMessage

def test_placeBuildingNonExistentBoardCoordinate(capsys):
    board = [["?", "BCH", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]]
    result = place_building("HSE", "a9", board)
    out, err = capsys.readouterr()
    expectedMessage = "Invalid location coordinates! Please enter in a valid location coordinate!\n"
    assert result == False and out[0:len(expectedMessage)] == expectedMessage

def test_placeBuildingNotOrthogonallyAdjacentToExistingBuilding(capsys):
    board = [["?", "BCH", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]]
    result = place_building("HSE", "c2", board)
    out, err = capsys.readouterr()
    expectedMessage = "You must build next to an existing building.\n"
    assert result == False and out[0:len(expectedMessage)] == expectedMessage

def test_placeBuildingOnAnExistingBuilding(capsys):
    board = [["?", "BCH", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]]
    location = "b1"
    result = place_building("HSE", location, board)
    out, err = capsys.readouterr()
    expectedMessage = "Invalid placement! There is already an existing building at " + location + ". Please enter in a different location!\n"
    assert result == False and out[0:len(expectedMessage)] == expectedMessage