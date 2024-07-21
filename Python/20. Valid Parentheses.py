# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        _dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        _stack = deque()
        for char in s:
            if char in _dict:
                _stack.append(char)
            else:
                if not _stack or char != _dict[_stack.pop()]:
                    return False

        return not bool(_stack)


s = "()[]{}"
X = Solution()
print(X.isValid(s))