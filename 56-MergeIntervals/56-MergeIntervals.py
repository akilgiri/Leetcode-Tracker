# Last updated: 5/25/2025, 1:08:28 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # If end of a previous interval end is greater then its next interval's start then they can be merged

        # First check if the start of the next interval is greater than its previous one
        merged = []
        intervals.sort(key = lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval
        merged.append(prev)
        return merged