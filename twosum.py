import os

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

"""
Brute Force Dictionary Solution #2

Input: 
array of numbers, target, k desired output values
Does not handle duplicate values

Output: 
Array of k tuples in order of proximity
k = 5 by default
returns None when there are no solutions

Procedure:
Iterate through each value
Input key: tuple of array values, value: proximity
Move range position to avoid redundant comparisons
Sort array and return top k values

Time Complexity:
O(nlogn) time
"""
def twoSum2(nums, target, k=5):
    # number dictionary
    numd = {}
    pos = 1
    for add in range(0, len(nums)-1): # n-1 iterations => O(n) x inner loop => O(n^2)
        for addend in range(add+1, len(nums)): # up to n-1 iterations => O(n)
            proximity = abs(target - (nums[add] + nums[addend]))
            print(nums[add], nums[addend], proximity)
            numd[(nums[add], nums[addend])] = proximity
    # this is heavy
    vals_by_prox = sorted(numd.items(), key=lambda val_prox: val_prox[1])  #, reverse=False)
    solutions = [val_prox[0] for val_prox in vals_by_prox]
    if not solutions:
        return None
    return solutions[:k]

if __name__ == "__main__":
    nums = [3, 9, 4, 7, 8, 9, 16, 1, 2, 15, 3, 17, 8, 5]
    print(twoSum2(nums, 17, 10))