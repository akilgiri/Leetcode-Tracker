# Last updated: 6/2/2025, 7:09:07 AM
class Solution:
    # def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    #     groups = defaultdict(list)
    #     result = []

    #     for i in range(len(nums)):
    #         for j in range(len(nums[i])):
    #             print(i,j)
    #             groups[i+j].append(nums[i][j])

    #     for g in groups.values():
    #         result += g[::-1]

    #     return result

    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(A)):
            for j in range(len(A[i])):
                d[i+j].append(A[i][j])
        return [v for k in d.keys() for v in reversed(d[k])]
