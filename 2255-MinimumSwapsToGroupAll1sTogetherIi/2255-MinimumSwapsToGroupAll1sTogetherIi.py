# Last updated: 5/25/2025, 1:08:13 PM
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # sliding window
        k = nums.count(1)

        # Add the first k elements to the sum to start
        curr_count = sum(nums[:k])
        max_count = sum(nums[:k])


        for i in range(len(nums)):
            curr_count -= nums[i]
            curr_count += nums[(i+k)%len(nums)]
            max_count = max(max_count, curr_count)

        return k - max_count

                