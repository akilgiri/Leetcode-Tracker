# Last updated: 5/25/2025, 1:08:33 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        # for char in s:
        #     if char in roman_to_int:
        #         res += roman_to_int[char]
        #         print(res)
        #     else:
        #         print("yeet")

        for i in range(len(s)):
            if i != len(s)-1 and s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                    res -= roman_to_int[s[i]]
            elif i != len(s)-1 and s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                res -= roman_to_int[s[i]]
            elif i != len(s)-1 and s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                res -= roman_to_int[s[i]]
            else:
                res += roman_to_int[s[i]]

        return res



    # def simp_roman(self, roman, roman_to_int):
        



    

        