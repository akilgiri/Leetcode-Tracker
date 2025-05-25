# Last updated: 5/25/2025, 1:08:28 PM
class Solution:
    def grayCode(self, n: int) -> List[int]:
        n = 1 << n
        result = []
        for i in range(n):
            result.append(i ^ (i >> 1))

        return result

        