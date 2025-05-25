# Last updated: 5/25/2025, 1:08:32 PM
class Solution:
    def isValid(self, s: str) -> bool:

        # stack = []

        # if len(s) <= 1:
        #     return False

        # for bracket in s:
        #     if bracket in "([{":
        #         stack.append(bracket)
        #     else:
        #         # print(f"Stack: {stack}, bracket: {bracket}")
        #         if bracket == ")" and stack.pop() != "(":
        #             return False
        #         elif bracket == "]" and stack.pop() != "[":
        #             return False
        #         elif bracket == "}" and stack.pop() != "{":
        #             return False
        #         else:
        #              return True
        
        # User a list as a stack
        # Push opening bracket to the stack
        # when encountering a closing bracket, pop from the stack, if it matches the bracket, then continue, otherwise notvalid

        stack = []

        # if len(s) <= 1:
        #     return False

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if len(stack) >= 1:
                    if char == ")" and stack.pop() == "(":
                        continue
                    elif char == "]" and stack.pop() == "[":
                        continue
                    elif char == "}" and stack.pop() == "{":
                        continue
                    else:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False