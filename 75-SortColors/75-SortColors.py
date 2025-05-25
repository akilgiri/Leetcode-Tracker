# Last updated: 5/25/2025, 1:08:27 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Red = 0
        # White = 1
        # Blue = 2

        colorFreq = {0:0, 1:0, 2:0}

        for color in nums:
            colorFreq[color] += 1

        for i in range(0, colorFreq[0]):
            nums[i] = 0
        for i in range(colorFreq[0], colorFreq[0]+colorFreq[1]):
            nums[i] = 1
        for i in range(colorFreq[0]+colorFreq[1], len(nums)):
            nums[i] = 2
        