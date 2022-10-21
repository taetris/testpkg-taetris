# Initial test file
import unittest
from src.sample1 import TextTransform as sample

class TestFunc(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(sample.lower("ALL SMALL"), "all small")
    def test_upper(self): 
        self.assertIn(sample.upper("all caps"), ["ALL CAPSS", "ALL CAPS"])
    def test_title(self): 
        self.assertTrue(sample.title("the HUNGRY fox")=="The Hungry Fox")
    def test_kebab(self): 
        print(sample.kebab("hyphen text coming right up"))

# sampleFunct(self)

if __name__ == '__main__':
    # import timeit
    # print(timeit.timeit("test()", setup="from __main__ import test", number=100))
    unittest.main()

# CODE TO RUN ALL TESTS AT ONCE: python -m unittest discover -s tests -t src