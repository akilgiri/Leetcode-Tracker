# Last updated: 6/1/2025, 10:33:24 AM
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
            # if color in colors:
            #     # colors[color].append(ball)
            #     colors[color] += 1
            # else:
            #     # colors[color] = [ball]
            #     colors[color] = 1

            balls[ball] = color
            # colors[ball] = color
            # print(colors, balls)
            result.append(len(colors))
        return result
