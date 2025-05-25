# Last updated: 5/25/2025, 1:08:15 PM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res+=1

        return res
        