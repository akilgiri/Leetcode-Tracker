# Last updated: 5/25/2025, 1:08:18 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        height = len(grid)
        width = len(grid[0])

        def dfs(r, c):
            if r<0 or r>=height or c<0 or c>=width or grid[r][c] == 0:
                return 1
            
            if grid[r][c] == 1:
                grid[r][c] = -1 # mark visited
                return dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

            return 0

        perimeter = 0
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 1:
                    perimeter += dfs(r,c)
                    break
        return perimeter

        