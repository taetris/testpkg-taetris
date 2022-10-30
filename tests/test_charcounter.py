import pytest
from src.charcounter import CharCount as cc

@pytest.fixture
def valInput():
    return "I am a huuman 8990."

def test_charcounter(valInput):
  assert cc.count(valInput)=={'i': 1, ' ': 4, 'a': 3, 'm': 2, 'h': 1, 'u': 2, 'n': 1, '8': 1, '9': 2, '0': 1, '.': 1}

    