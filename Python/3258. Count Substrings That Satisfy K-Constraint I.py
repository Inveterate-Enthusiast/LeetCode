# You are given a binary string s and an integer k.
#
# A binary string satisfies the k-constraint if either of the following conditions holds:
#
# The number of 0's in the string is at most k.
# The number of 1's in the string is at most k.
# Return an integer denoting the number of substrings of s that satisfy the k-constraint.

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left, result = 0, 0
        i, j = 0, 0
        for right in range(len(s)):
            if s[right] == "1":
                i += 1
            else:
                j += 1

            while i > k and j > k:
                if s[left] == "1":
                    i -= 1
                else:
                    j -= 1
                left += 1
            result += right - left + 1
        return result




s = "10101"
k = 1
x = Solution()
print(x.countKConstraintSubstrings(s, k))