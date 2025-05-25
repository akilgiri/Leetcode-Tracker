# Last updated: 5/25/2025, 1:08:06 PM
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        left = 0
        result = 0
        for right in range(2, len(nums)):
            if nums[left] + nums[right] == nums[left+1]/2:
                result+=1
            left += 1
        return result
        