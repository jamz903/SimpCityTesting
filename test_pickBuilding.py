import pytest
from pick_buildings import *

def test_pickBuildings():

    building_types = ["HSE", "BCH", "FAC", "SHP", "HWY"]

    buildings_list = [
        "HSE", "HSE", "HSE", "HSE", "HSE", "HSE", "HSE", "HSE",
        "BCH", "BCH", "BCH", "BCH", "BCH", "BCH", "BCH", "BCH",
        "FAC", "FAC", "FAC", "FAC", "FAC", "FAC", "FAC", "FAC",
        "SHP", "SHP", "SHP", "SHP", "SHP", "SHP", "SHP", "SHP",
        "HWY", "HWY", "HWY", "HWY", "HWY", "HWY", "HWY", "HWY"
    ]

    ori_size = len(buildings_list)

    result = pick_buildings(buildings_list)
    assert result[0] in building_types and result[1] in building_types and len(buildings_list) == (ori_size - 2)