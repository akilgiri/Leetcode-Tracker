# Last updated: 5/25/2025, 1:08:24 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j] < target:
                i+=1
            elif numbers[i]+numbers[j] > target:
                j-=1
            else:
                return[i+1, j+1]



