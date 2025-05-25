# Last updated: 5/25/2025, 1:08:16 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + ( (high-low) // 2 )

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1

        return -1
        
        