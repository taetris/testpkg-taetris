import pytest
from src.charcounter import CharCount as cc

def test_normal():
  sentence = "I am hooman 9067."
  assert cc.count(sentence)['m']== 2

