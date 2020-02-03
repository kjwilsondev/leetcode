import unittest
from largest_value import largestValue, largestValue2

class LargestValueTest(unittest.TestCase):
    def test_positive_integer_array(self):
        nums = [5, 3, 6, 8, 2, 4, 7]
        assert largestValue(nums, 3) == [6, 8, 7]

class LargestValue2Test(unittest.TestCase):
    def test_positive_integer_array(self):
        nums = [5, 3, 6, 8, 2, 4, 7]
        assert largestValue2(nums, 3) == [6, 8, 7]

if __name__ == '__main__':
    unittest.main()