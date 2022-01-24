import pytest
from see_remaining_buildings import *

def test_seeRemainingBuildings(capsys):

    buildings_list = [
        "HSE", "HSE", "HSE", "HSE", "HSE",                          # 5 HSE
        "BCH", "BCH", "BCH", "BCH", "BCH", "BCH", "BCH",            # 7 BCH
        "FAC", "FAC", "FAC", "FAC", "FAC", "FAC", "FAC", "FAC",     # 8 FAC
        "SHP", "SHP", "SHP", "SHP",                                 # 4 SHP
        "HWY", "HWY", "HWY", "HWY", "HWY", "HWY"                    # 6 HWY
    ]
    see_remaining_buildings(buildings_list)

    out, err = capsys.readouterr()
    expectedOutput = "Building          Remaining\n--------          ---------\nHSE               5\nBCH               7\nFAC               8\nSHP               4\nHWY               6\n"
    assert out == expectedOutput
    