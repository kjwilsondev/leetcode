import os

"""
Sorted Solution
O(nlogn)
"""
def largestValue(nums, k):
    # sort_nums = sorted(nums)
    # return sort_nums[:k]
    return sorted(nums)[:k]

if __name__ == "__main__":
    nums = [3, 9, 4, 7, 8, 9]
    # print(largestValue(nums, 3)) # [3, 4, 7]
    print(largestValue2(nums, 3))