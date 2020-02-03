import os

"""
Sorted Solution
O(nlogn)
"""
def largestValue(nums, k):
    return sorted(nums)[-k:]

if __name__ == "__main__":
    # TESTS
    nums = [3, 9, 4, 7, 8, 9]
    print(largestValue(nums, 3)) # [8, 9, 9]
    nums = [5, 3, 6, 8, 2, 4, 7]
    print(largestValue(nums, 4)) # [5, 6, 7, 8]
    print(distance)