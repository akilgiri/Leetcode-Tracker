# Last updated: 5/25/2025, 1:08:09 PM
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors =  [0] * n
        result = []
        count = 0

        # Set colors[index] to color
        # Count the number of adjacent pairs in colors which have the same color

        for i , color in queries:
            # Check if same color before update
            if i > 0 and colors[i-1] != 0 and colors[i-1] == colors[i]:
                count -= 1  
            if i < n-1 and colors[i+1] != 0 and colors[i+1] == colors[i]:
                count -= 1

            colors[i] = color

            if i > 0 and colors[i-1] == colors[i]:
                count += 1  
            if i < n-1 and colors[i+1] == colors[i]:
                count += 1

            result.append(count)

        return result

            
        