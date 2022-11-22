from src.naruto import *
import pytest 

def test_saga():
    assert saga() == {'s1 Kazekage Rescue': 32, 's2 Long-Awaited Reunion': 21, 's3 Twelve Guardian Ninja': 18, 's4 Immortal Devastators': 17, 's5 The Three-Tailed Demon Turtle': 12}

def test_rates():
    assert rates() == {'Above 8': 28, 'Between 7 and 8': 46, 'Between 6 and 7': 26}

def test_no_of_types_in_year():
    assert no_of_types_in_year() == "{'2007': defaultdict(<class 'int'>, {'Mixed Canon/Filler': 21, 'Manga Canon': 19, 'Filler': 1}), '2008': defaultdict(<class 'int'>, {'Manga Canon': 27, 'Mixed Canon/Filler': 7, 'Filler': 15}), '2009': defaultdict(<class 'int'>, {'Filler': 10})}"

def test_total_votes_in_year():
    assert total_votes_in_year() == {'2007': 18112, '2008': 17851, '2009': 2463}