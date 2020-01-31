import unittest
from twosum import twoSum

class TwoSumTest(unittest.TestCase):
    # two sum returns first pair to equal target
    def test_positive_integer_array(self):
        nums = [3, 2, 4]
        assert twoSum(nums, 6) == (2,4)
        nums = [3, 4, 4, 7, 8, 9]
        assert twoSum(nums, 17) == (8,9)
    
    def test_no_pair_found(self):
        nums = [3, 2, 4]
        assert twoSum(nums, 10) is None
        nums = [3, 4, 4, 7, 8, 9]
        assert twoSum(nums, 20) is None

class TwoSumTest(unittest.TestCase):
    # two sum returns first pair to equal target
    def test_positive_integer_array(self):
        nums = [3, 2, 4]
        assert twoSum(nums, 6) == (2,4)
        
if __name__ == '__main__':
    unittest.main()