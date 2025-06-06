# Last updated: 5/25/2025, 1:08:32 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left-1] and left<right:
                        left += 1
                
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1

        return triplets
        