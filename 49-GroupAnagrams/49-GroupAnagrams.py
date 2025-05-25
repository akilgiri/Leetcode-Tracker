# Last updated: 5/25/2025, 1:08:30 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringmap = {}
        res = []
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in stringmap:
                stringmap[sorted_s].append(s)
            else:
                stringmap[sorted_s] = [s]
        
        return list(stringmap.values())
        # for s in stringmap:
        #     res.append(stringmap[s])
        # return res




        