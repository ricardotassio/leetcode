#Important points:
#1. Stack
#2. Hashmap
# The Hashmap should have the closing tags as keys and the opening tags as values
# We should check if the character inside the loop is closed, if not append.
# If yes, check if the stack is empty, if not, check if the last element in the stack is equal to the value of the key in the hashmap.
# If yes, pop the last element in the stack, otherwise return False.
# If the stack is empty, return True, otherwise return False.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

test = Solution()
print(test.isValid("{([])}"))
print(test.isValid("()"))
print(test.isValid("[]"))
print(test.isValid("{[}"))
print(test.isValid("{{()}}"))
print(test.isValid("[])"))