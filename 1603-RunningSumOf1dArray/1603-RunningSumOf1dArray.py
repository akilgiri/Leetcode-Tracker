# Last updated: 5/25/2025, 1:08:13 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out_nums = []
        num = 0
        for i in nums:
            print(i, num)
            out_nums.append(i+num)
            num = i+num

        return out_nums