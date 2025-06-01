# Last updated: 6/1/2025, 10:01:04 AM
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        result = []
        indexes = []
        for n in range(len(nums)):
            if nums[n] == x:
                indexes.append(n)

        for q in queries:
            if q > len(indexes):
                result.append(-1)
            else:
                result.append(indexes[q-1])
        



        return result
            



        