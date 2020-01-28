import os

# Brute Force Solution
def twoSum(nums, target):
        pos = 1
        for add in range(0, len(nums)-1):
            # print(f"add {nums[add]}")
            for addend in range(pos, len(nums)):
                # print(f"addend {addend, nums[addend]}")
                if (nums[add] + nums[addend]) == target:
                    return [add, addend]
            pos += 1

# Dictionary Solution
# Put number in dictionary, check if counterpart is there
        

if __name__ == "__main__":
    # TEST 1
    # nums = [3, 2, 4]
    # print(twoSum(nums, 6))

    # TEST 2
    nums = [3, 4, 4, 7, 8, 9]
    print(twoSum(nums, 20))