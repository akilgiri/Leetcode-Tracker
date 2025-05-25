# Last updated: 5/25/2025, 1:08:07 PM
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinctnum = len(set(nums))
        count = 0
        frequency = Counter()
        left = 0

        for right in range(len(nums)):
            frequency[nums[right]] +=1
            
            while len(frequency) == distinctnum:
                count += (len(nums) - right)
                frequency[nums[left]] -= 1

                if frequency[nums[left]] == 0:
                    del frequency[nums[left]]
                left += 1

        return count
        