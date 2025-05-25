# Last updated: 5/25/2025, 1:08:35 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for i in range(len(nums)):
            if target-nums[i] in elements:
                return [elements[target-nums[i]], i]
            elements[nums[i]] = i


            

