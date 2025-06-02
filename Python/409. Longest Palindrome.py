# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        our_set = set()
        for i in s:
            if i not in our_set:
                our_set.add(i)
            else:
                our_set.discard(i)
        if len(our_set):
            return len(s) - len(our_set) + 1
        else:
            return len(s)

s = "abccccdd"
x = Solution()
print(x.longestPalindrome(s))