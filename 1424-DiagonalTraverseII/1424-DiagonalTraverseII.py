# Last updated: 6/2/2025, 7:08:06 AM
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        result = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                print(i,j)
                groups[i+j].append(nums[i][j])
        print(groups)

        for g in groups.values():
            result += g[::-1]

        return result
