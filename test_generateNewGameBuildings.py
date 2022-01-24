import pytest
from generate_new_game_buildings import *

def test_generateNewGameBuildings():
    result = generate_new_game_buildings()
    expectedResult = [
        "HSE", "HSE", "HSE", "HSE", "HSE", "HSE", "HSE", "HSE",
        "BCH", "BCH", "BCH", "BCH", "BCH", "BCH", "BCH", "BCH",
        "FAC", "FAC", "FAC", "FAC", "FAC", "FAC", "FAC", "FAC",
        "SHP", "SHP", "SHP", "SHP", "SHP", "SHP", "SHP", "SHP",
        "HWY", "HWY", "HWY", "HWY", "HWY", "HWY", "HWY", "HWY"
    ]

    assert result.sort() == expectedResult.sort()
    