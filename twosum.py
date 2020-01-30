import os

"""
Brute Force Solution

Input: array of numbers, target
Output: first pair of numbers that add up to target

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
Dictionary Solution

Input: 
array of numbers, target

Output: 
Array of tuples that add up to target

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
    return solutions
        

if __name__ == "__main__":
    nums = [3, 4, 4, 7, 8, 9, 10]
    print(twoSum_dict(nums, 17))