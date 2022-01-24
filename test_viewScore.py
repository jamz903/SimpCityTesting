import pytest
view_score = pytest.importorskip("view_score")
from view_score import *

def test_viewScore_EmptyBoard(capsys):
    expectedOutput = "HSE: 0\nFAC: 0\nSHP: 0\nHWY: 0\nBCH: 0\nTotal score: 0\n"
    score = view_score([["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]])
    out, err = capsys.readouterr()
    assert score == 0 and out == expectedOutput

def test_viewScore_BCH(capsys):
    expectedOutput = "HSE: 0\nFAC: 0\nSHP: 0\nHWY: 0\nBCH: 3 + 3 + 1 = 7\nTotal score: 7\n"
    score = view_score([["BCH", "?", "?", "?"], ["?", "?", "?", "BCH"], ["?", "?", "?", "?"], ["?", "BCH", "?", "?"]])
    out, err = capsys.readouterr()
    assert score == 7 and out == expectedOutput

def test_viewScore_FAC_Case1(capsys):
    expectedOutput = "HSE: 0\nFAC: 3 + 3 + 3 = 9\nSHP: 0\nHWY: 0\nBCH: 0\nTotal score: 9\n"
    score = view_score([["FAC", "?", "?", "?"], ["?", "?", "FAC", "?"], ["?", "FAC", "?", "?"], ["?", "?", "?", "?"]])
    out, err = capsys.readouterr()
    assert score == 9 and out == expectedOutput

def test_viewScore_FAC_Case2(capsys):
    expectedOutput = "HSE: 0\nFAC: 4 + 4 + 4 + 4 + 1 = 17\nSHP: 0\nHWY: 0\nBCH: 0\nTotal score: 17\n"
    score = view_score([["FAC", "?", "FAC", "?"], ["?", "?", "?", "FAC"], ["?", "?", "?", "FAC"], ["?", "FAC", "?", "?"]])
    out, err = capsys.readouterr()
    assert score == 17 and out == expectedOutput

def test_viewScore_HSE_Case1(capsys):
    expectedOutput = "HSE: 1 = 1\nFAC: 1 = 1\nSHP: 0\nHWY: 0\nBCH: 0\nTotal score: 2\n"
    score = view_score([["?", "HSE", "?", "?"], ["?", "FAC", "?", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]])
    out, err = capsys.readouterr()
    assert score == 2 and out == expectedOutput


def test_viewScore_HSE_Case2(capsys):
    expectedOutput = "HSE: 1 + 4 = 5\nFAC: 0\nSHP: 1 = 1\nHWY: 0\nBCH: 1 = 1\nTotal score: 7\n"
    score = view_score([["?", "HSE", "?", "?"], ["SHP", "HSE", "BCH", "?"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]])
    out, err = capsys.readouterr()
    assert score == 7 and out == expectedOutput

def test_viewScore_SHP_Case1(capsys):
    expectedOutput = "HSE: 0\nFAC: 1 = 1\nSHP: 1 = 1\nHWY: 0\nBCH: 0\nTotal score: 2\n"
    score = view_score([["?", "?", "?", "?"], ["?", "?", "SHP", "?"], ["?", "?", "FAC", "?"], ["?", "?", "?", "?"]])
    out, err = capsys.readouterr()
    assert score == 2 and out == expectedOutput

def test_viewScore_SHP_Case2(capsys):
    expectedOutput = "HSE: 0\nFAC: 1 = 1\nSHP: 2 = 2\nHWY: 0\nBCH: 1 = 1\nTotal score: 4\n"
    score = view_score([["?", "?", "?", "?"], ["?", "BCH", "SHP", "?"], ["?", "?", "FAC", "?"], ["?", "?", "?", "?"]])
    out, err = capsys.readouterr()
    assert score == 4 and out == expectedOutput

def test_viewScore_HWY_Case1(capsys):
    expectedOutput = "HSE: 0\nFAC: 0\nSHP: 0\nHWY: 1 + 1 + 1 = 3\nBCH: 0\nTotal score: 3\n"
    score = view_score([["?", "?", "HWY", "?"], ["?", "?", "HWY", "?"], ["?", "?", "HWY", "?"], ["?", "?", "?", "?"]])
    out, err = capsys.readouterr()
    assert score == 3 and out == expectedOutput

def test_viewScore_HWY_Case2(capsys):
    expectedOutput = "HSE: 0\nFAC: 0\nSHP: 0\nHWY: 3 + 3 + 3 = 9\nBCH: 0\nTotal score: 9\n"
    score = view_score([["?", "?", "?", "?"], ["?", "HWY", "HWY", "HWY"], ["?", "?", "?", "?"], ["?", "?", "?", "?"]])
    out, err = capsys.readouterr()
    assert score == 9 and out == expectedOutput

def test_fullBoard_Case1(capsys):
    expectedOutput = "HSE: 1 + 5 + 5 + 3 + 3 = 17\nFAC: 1 = 1\nSHP: 2 + 2 + 3 = 7\nHWY: 4 + 4 + 4 + 4 = 16\nBCH: 3 + 3 + 3 = 9\nTotal score: 50\n"
    score = view_score([["SHP", "SHP", "HSE", "FAC"], ["BCH", "HSE", "HSE", "BCH"], ["BCH", "SHP", "HSE", "HSE"], ["HWY", "HWY", "HWY", "HWY"]])
    out, err = capsys.readouterr()
    assert score == 50 and out == expectedOutput

def test_fullBoard_Case2(capsys):
    expectedOutput = "HSE: 4 + 3 + 1 = 8\nFAC: 3 + 3 + 3 = 9\nSHP: 2 + 3 = 5\nHWY: 3 + 3 + 3 + 1 + 2 + 2 = 14\nBCH: 3 + 3 = 6\nTotal score: 42\n"
    score = view_score([["HWY", "HWY", "HWY", "FAC"], ["BCH", "HSE", "HSE", "SHP"], ["BCH", "SHP", "HSE", "FAC"], ["HWY", "FAC", "HWY", "HWY"]])
    out, err = capsys.readouterr()
    assert score == 42 and out == expectedOutput