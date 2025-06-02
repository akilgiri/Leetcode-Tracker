# Last updated: 6/2/2025, 7:11:15 AM
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        result = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                groups[i+j].append(nums[i][j])

        for g in groups:
            result += (groups[g][::-1])
        return result

