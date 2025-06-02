# Last updated: 6/2/2025, 6:14:18 AM
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groups = defaultdict(list)
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows-1):
            for j in range(cols-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True



        