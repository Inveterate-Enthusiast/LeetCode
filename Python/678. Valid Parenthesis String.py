# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
#
# The following rules define a valid string:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
from collections import deque
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        left = "("; right = ")"; ast = "*"
        _dict = {"(": deque(), "*": deque()}
        for index, char in enumerate(s):
            if char == left: _dict[char].append(index)
            if char == ast: _dict[char].append(index)

            if char == right:
                if _dict[left]:
                    _dict[left].pop()
                elif _dict[ast]:
                    _dict[ast].pop()
                else:
                    return False

        while _dict[left] and _dict[ast]:
            while (_dict[ast] and _dict[left]) and _dict[ast][0] < _dict[left][0]:
                _dict[ast].popleft()
            if (_dict[ast] and _dict[left]):
                _dict[ast].popleft(); _dict[left].popleft()

        return not _dict["("]



s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
X = Solution()
print(X.checkValidString(s))





