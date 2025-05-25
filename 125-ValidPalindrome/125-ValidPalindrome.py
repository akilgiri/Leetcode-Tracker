# Last updated: 5/25/2025, 1:08:25 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for letter in s.lower():
            if letter.isalnum():
                s2+=letter
        return s2 == s2[::-1]

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # .isalnum() can be used to check if a char is alphanumeric
#         s = s.replace(" ", "")
#         s = s.lower()
#         for char in s:
#             if not char.isalnum():
#                 s = s.replace(char, "")
#         return s == s[::-1]
