# Given a string s, reverse the string according to the following rules:
#
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = {chr(i) for i in range(65, (90 + 1))}.union({chr(j) for j in range(97, (122 + 1))})
        ss = [i for i in s]
        n = len(ss)
        i, j = 0, (n - 1)
        while i < j:
            if ss[i] in letters:
                while (j > i) and not ss[j] in letters:
                    j -= 1
                if i < j:
                    ss[i], ss[j] = ss[j], ss[i]
                    i, j = (i + 1), (j - 1)
                else:
                    break
            else:
                i += 1
        return "".join(ss)

s = "7_28]"
x = Solution()
print(x.reverseOnlyLetters(s))