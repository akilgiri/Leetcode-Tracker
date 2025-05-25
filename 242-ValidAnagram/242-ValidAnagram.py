# Last updated: 5/25/2025, 1:08:20 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = defaultdict(int)
        
        for char in s:
            counter[char] += 1
        for char in t:
            counter[char] -= 1

        for count in counter.values():
            if count != 0:
                return False
        return True
        



        # count = defaultdict(int)
        # if len(s) != len(t):
        #     return False
            
        # for c in s:
        #     count[c] += 1
        
        # for c in t:
        #     count[c] -= 1

        # for val in count.values():
        #     if  val != 0:
        #         return False

        # return True


        