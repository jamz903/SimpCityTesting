import pytest
from convert_board_coords_to_index import *

@pytest.mark.parametrize("board_coords, expectedResult", 
[("a1", [0,0]), ("b2", [1,1]), ("d3", [2,3])])
def test_convertBoardCoordsToIndex(board_coords, expectedResult):
    result = convert_board_coords_to_index(board_coords)
    assert result == expectedResult