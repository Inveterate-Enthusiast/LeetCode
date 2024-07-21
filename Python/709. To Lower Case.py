# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.


class Solution:
    def toLowerCase1(self, s: str) -> str:
        return s.lower()




s = "Hello"
X = Solution()
print(X.toLowerCase1(s))