import os
from collections import Counter

"""
Brute Force Solution

Input: 
array of numbers, target

Output: 
first pair of numbers that add up to target
returns None when there are no solutions

Procedure:
Iterate through each value
Compare it to each value in array
Move range position to avoid redundant comparisons

Time Complexity:
O(nlogn) time
"""
def twoSum(nums, target):
        pos = 1
        for add in range(0, len(nums)-1):
            print(f"add {nums[add]}")
            for addend in range(pos, len(nums)):
                print(f"addend {addend, nums[addend]}")
                if (nums[add] + nums[addend]) == target:
                    return (nums[add], nums[addend])
            print(pos)
            pos += 1
        return None

"""
Pointer Solution

Input: 
array of numbers, target

Output: 
first pair of numbers that add up to target
returns None when there are no solutions

Procedure:
Sort array
Set while loop to stop when pointers cross
Compare sum to target
If too small move left pointer
If too big move right pointer
If target hit move both pointers
Return solution

Time Complexity:
O(nlogn) time
"""
def twoSum_point(nums, target):
    # number dictionary
    nums = sorted(nums) # O(nlogn)
    left, right = 0, len(nums) - 1
    while left < right: # O(n)
        # print("left", nums[left])
        # print("right", nums[right])
        if (nums[left] + nums[right]) > target:
            right -= 1
        elif (nums[left] + nums[right]) < target:
            left += 1
        elif (nums[left] + nums[right]) == target:
            return (nums[left], nums[right])
    return None

"""
Dictionary Solution

Input: 
array of numbers, target

Output: 
Array of tuples that add up to target
returns None when there are no solutions

Procedure:
Iterate through each value
Check if target counterpart is in dictionary
Add value to dictionary

Time Complexity:
O(n) time
"""
def twoSum_dict(nums, target):
    # number dictionary
    numd = {}
    solutions = []
    for add in nums: # O(n)
        print(numd)
        if (target - add) in numd: # O(1)
            numd[target-add] -= 1
            solutions.append((add, target-add))
        if add in numd: # O(1)
            numd[add] += 1
        else:
            numd[add] = 1
    if not solutions:
        return None
    return solutions
        

if __name__ == "__main__":
    nums = [3, 9, 4, 7, 8, 9]
    print(twoSum_point(nums, 17))