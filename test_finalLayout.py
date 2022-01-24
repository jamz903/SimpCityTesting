import pytest
final_layout = pytest.importorskip("final_layout")
from final_layout import *

def test_finalLayout_Case1(capsys):
    expectedOutput = "\nFinal layout of Simp City:\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1| SHP | SHP | HSE | FAC |\n  +-----+-----+-----+-----+\n 2| BCH | HSE | HSE | BCH |\n  +-----+-----+-----+-----+\n 3| BCH | SHP | HSE | HSE |\n  +-----+-----+-----+-----+\n 4| HWY | HWY | HWY | HWY |\n  +-----+-----+-----+-----+\nHSE: 1 + 5 + 5 + 3 + 3 = 17\nFAC: 1 = 1\nSHP: 2 + 2 + 3 = 7\nHWY: 4 + 4 + 4 + 4 = 16\nBCH: 3 + 3 + 3 = 9\nTotal score: 50\n"
    final_layout([["SHP", "SHP", "HSE", "FAC"], ["BCH", "HSE", "HSE", "BCH"], ["BCH", "SHP", "HSE", "HSE"], ["HWY", "HWY", "HWY", "HWY"]])
    out, err = capsys.readouterr()
    assert out == expectedOutput

def test_finalLayout_Case2(capsys):
    expectedOutput = "\nFinal layout of Simp City:\n     A     B     C     D   \n  +-----+-----+-----+-----+\n 1| HWY | HWY | HWY | FAC |\n  +-----+-----+-----+-----+\n 2| BCH | HSE | HSE | SHP |\n  +-----+-----+-----+-----+\n 3| BCH | SHP | HSE | FAC |\n  +-----+-----+-----+-----+\n 4| HWY | FAC | HWY | HWY |\n  +-----+-----+-----+-----+\nHSE: 4 + 3 + 1 = 8\nFAC: 3 + 3 + 3 = 9\nSHP: 2 + 3 = 5\nHWY: 3 + 3 + 3 + 1 + 2 + 2 = 14\nBCH: 3 + 3 = 6\nTotal score: 42\n"
    final_layout([["HWY", "HWY", "HWY", "FAC"], ["BCH", "HSE", "HSE", "SHP"], ["BCH", "SHP", "HSE", "FAC"], ["HWY", "FAC", "HWY", "HWY"]])
    out, err = capsys.readouterr()
    assert out == expectedOutput