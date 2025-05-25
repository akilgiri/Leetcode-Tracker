# Last updated: 5/25/2025, 1:08:29 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        # for i in range(len(nums)):

        #     if currSum + nums[i] < 0:
        #         currSum = 0
        #         # maxSum = 0
        #     else:
        #         currSum = currSum + nums[i]
        #     maxSum = max(maxSum, currSum)

            # else:
            #     maxSum = currSum
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(maxSum, currSum)

            print(f"Curr Sum: {currSum}, Max Sum: {maxSum}")

        return maxSum