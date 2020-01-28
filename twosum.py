class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = 1
        for add in range(0, len(nums)-1):
            print(add)
            for addend in range(pos, len(nums)-1):
                print(addend)
                if (nums[add] + nums[addend]) == target:
                    return [add, addend]
            pos += 1
        return "No match found"