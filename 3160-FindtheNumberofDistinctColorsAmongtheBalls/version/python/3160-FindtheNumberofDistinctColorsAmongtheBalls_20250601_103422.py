# Last updated: 6/1/2025, 10:34:22 AM
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        currCount = 0
        colors = {}
        balls = {}
        result = []
        for q in queries:
            ball = q[0]
            color = q[1]
            if ball in balls:
                colors[balls[ball]] -= 1
                if colors[balls[ball]] == 0:
                    del colors[balls[ball]]

            colors[color] = colors.get(color, 0) + 1
            balls[ball] = color
            result.append(len(colors))
        return result
