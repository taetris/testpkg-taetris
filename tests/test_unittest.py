# # Initial test file
# import unittest
# from src.sample1 import TextTransform as sample
    
# class TestFunc1(unittest.TestCase):
#     def test_lower(self): 
#         self.assertEqual(sample.t_lower("ALL SMALL"), "all small")
#     def test_upper(self): 
#         self.assertIn(sample.t_upper("all caps"), ["ALL CAPSS", "ALL CAPS"])
#     def test_title(self): 
#         self.assertTrue(sample.t_title("the HUNGRY fox")=="The Hungry Fox")
#     def test_kebab(self): 
#         self.assertEqual(sample.t_kebab("hyphen text coming right up"), "hyphen-text-coming-right-up")
    
# class addedTest(unittest.TestCase):
#     def test_reverse(self):
#         self.assertEqual(sample.reverse("1234567"), "7654321")

# if __name__ == '__main__':
#     unittest.main()

# # CODE TO RUN UNIT TESTS AT ONCE: python -m unittest discover 