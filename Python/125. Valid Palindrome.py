# A phrase is a palindrome if,
# after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome1(self, s: str) -> bool:
        left = 0; right = len(s)-1
        while left <= right:
            while left < right and not s[left].isalpha() and not s[left].isnumeric():
                left += 1
            while right > left and not s[right].isalpha() and not s[right].isnumeric():
                right -= 1
            a = s[left].lower() if s[left].isalpha() else (s[left] if s[left].isnumeric() else None)
            b = s[right].lower() if s[right].isalpha() else (s[right] if s[right].isnumeric() else None)
            if left <= right and a != b:
                return False
            left += 1; right -= 1
        return True

    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        left = 0; right = len(s)-1
        while left <= right:
            while left < right and not s[left].isalpha() and not s[left].isnumeric():
                left += 1
            while right > left and not s[right].isalpha() and not s[right].isnumeric():
                right -= 1
            if left <= right and s[left] != s[right]:
                return False
            left += 1; right -= 1
        return True


s = "123A54 man, a plan, a canal: Panam45a321"
X = Solution()
print(X.isPalindrome2(s))