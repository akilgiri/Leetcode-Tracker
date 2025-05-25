# Last updated: 5/25/2025, 1:08:24 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique_nums = set(nums)

        curr_num = 0
        curr_streak = 0
        max_streak = 0

        for i in unique_nums:
            if i-1 not in unique_nums:
                curr_num = i
                curr_streak = 1

                while curr_num+1 in unique_nums:
                    curr_num += 1
                    curr_streak+=1

                max_streak = max(max_streak, curr_streak)

        return max_streak



        