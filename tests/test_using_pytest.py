import pytest
from src.first import result_get, new, incomes, prime, palindrome

@pytest.fixture
def get_string():
  return 'iamritik'

def test_prime_num():
    assert prime(9) == False

def test_new():
    assert new(incomes) == {'Books': 3970.0, 'Tutorials': 1940.0, 'Courses': 7680.0}

def test_answer():
    assert result_get(get_string) == {'i': 3, 'a': 1, 'm': 1, 'r': 1, 't': 1, 'k': 1}

@pytest.mark.parametrize("test_data",[ 
    'a',
    'bob',
    '111',
    'Never odd or even'
    ])

def test_palindrome(test_data):
    assert palindrome(test_data) 

@pytest.mark.parametrize("not_pt",['123','Never'])

def test_palindrome_not(not_pt):
    assert not palindrome(not_pt) 