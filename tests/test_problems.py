import pytest
from src.problems import two_sum, roman_to_integer, longest_prefix, valid_parenthesis

def test_two_sum():
    assert two_sum([2,7,11,15],9) == [0,1]

@pytest.mark.parametrize('testdata, result',
                        [('LVIII', 58),
                         ('MCMXCIV', 1994),
                         ('III', 3)])

def test_roman_to_integer(testdata,result):
    assert roman_to_integer(testdata) == result


@pytest.mark.parametrize('test,ans',[
    (["flower","flow","flight"],"fl"),
    (["dog","racecar","car"],"")
])

def test_longest_prefix(test,ans):
    assert longest_prefix(test) == ans

@pytest.mark.parametrize('data,bool',[
    ('()',True),
    ('(){}[]',True),
    ('(]',False)
])

def test_valid_parenthesis(data,bool):
    assert valid_parenthesis(data) == bool