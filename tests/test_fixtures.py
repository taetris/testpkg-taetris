
import pytest
from src.sample1 import TextTransform as s

@pytest.fixture
def valInput():
    return "pYtesT fixture TESTING"

def test_lower(valInput): 
    assert s.t_lower(valInput)== "pytest fixture testing"

def test_upper(valInput): 
    assert s.t_upper(valInput)=="PYTEST FIXTURE TESTING"

def test_title(valInput): 
    assert s.t_title(valInput) == "Pytest Fixture Testing"

def test_kebab(valInput):
    assert s.t_kebab(valInput) =="pytest-fixture-testing"


