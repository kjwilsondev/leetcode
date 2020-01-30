import os

# Brute Force Solution
# Iterate through each value
# Compare it to each value in array
# Move range position to avoid redundant comparisons
# O(nlogn) time
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

# Dictionary Solution
# Put number in dictionary, check if counterpart is there
# O(n) time
def twoSum_dict(nums, target):
    # number dictionary
    numd = {}
    for add in nums:
        

if __name__ == "__main__":
    nums = [3, 4, 4, 7, 8, 9]
    print(twoSum(nums, 17))