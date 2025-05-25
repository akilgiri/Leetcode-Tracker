# Last updated: 5/25/2025, 1:08:34 PM
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     # parse string until you find a repeated character

    #     if len(s.strip(" ")) < 1:
    #         s_length = 0
    #         if s == "":
    #             s_length = 0
    #         else:
    #             s_length = 1
    #         return s_length
    #     subString = ""
    #     subString_lengths = []

    #     for i in range(len(s)):
    #         for j in range(i, len(s)):
    #             if s[j] not in subString:
    #                 subString += s[j]
    #             else:
    #                 subString_lengths.append(len(subString))
    #                 subString = ""
    #                 break

    #     if len(subString_lengths) > 1:
    #         return max(subString_lengths)
    #     else:
    #         return len(s)
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength    
        