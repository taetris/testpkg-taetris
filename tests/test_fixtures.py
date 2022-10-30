
import pytest
from src.sample1 import TextTransform as s

@pytest.mark.parametrize("valInput, valOutput", [
    ("a", "a"),
    ("pYtesT fixture TESTING","pytest fixture testing"),
    ("A: b c!", "a: b c!"),
])

def test_lower(valInput, valOutput): 
    assert s.t_lower(valInput) == valOutput

@pytest.fixture
def valInput2():
    return "pYtesT fixture TESTING"

def test_upper(valInput2): 
    assert s.t_upper(valInput2)=="PYTEST FIXTURE TESTING"

def test_title(valInput2): 
    assert s.t_title(valInput2) == "Pytest Fixture Testing"

def test_kebab(valInput2):
    assert s.t_kebab(valInput2) =="pytest-fixture-testing"


