# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
#
# If there are fewer than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters,
# then reverse the first k characters and leave the other as original.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = str()
        left, right = 0, k
        i = 1
        while (left < right) and (right < len(s)):
            if (i % 2) != 0:
                result += ''.join(reversed(s[left:right]))
            else:
                result += s[left:right]
            left, right = right, right + k
            i += 1
        else:
            if left < len(s):
                if (i % 2) != 0:
                    result += ''.join(reversed(s[left:]))
                else:
                    result += s[left:]

        return result

s = "abcdefg"
k = 2
x = Solution()
print(x.reverseStr(s, k))