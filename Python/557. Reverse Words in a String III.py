# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(" ")
        result = " ".join([''.join(reversed(i)) for i in ss])
        return result

s = "Let's take LeetCode contest"
x = Solution()
print(x.reverseWords(s))