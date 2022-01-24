import pytest
from view_high_score import *


def test_view_highscore_with_highscore(capsys, monkeypatch):

    file = open("SimpCityLeaderboard.csv", "w")
    for i in range(24):
        file.write("\n")

    file.write(
        "qixun:60, justin:90, junwei:70, jamie:80, rhys:130, gamer123:100, testgamer:25\n")

    file.close()

    monkeypatch.setattr('builtins.input', lambda _: "5,5")
    view_high_score()
    out, err = capsys.readouterr()
    assert out == "--------- HIGH SCORES ---------\n"
