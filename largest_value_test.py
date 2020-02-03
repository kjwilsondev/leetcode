import unittest
from largest_value import largestValue

class LargestValueTest(unittest.TestCase):
    def test_positive_integer_array(self):
        nums = [5, 3, 6, 8, 2, 4, 7]
        print(sorted(nums))
        print(sorted(nums)[-3:])
        assert largestValue(nums, 3) == [6, 7, 8]

if __name__ == '__main__':
    unittest.main()