# Given a 0-indexed string word and a character ch,
# reverse the segment of word that starts at index 0
# and ends at the index of the first occurrence of ch (inclusive).
# If the character ch does not exist in word, do nothing.
#
# For example, if word = "abcdefd" and ch = "d",
# then you should reverse the segment that starts at 0 and ends at 3 (inclusive).
# The resulting string will be "dcbaefd".
# Return the resulting string.


class Solution:
    def reversePrefix1(self, word: str, ch: str) -> str:
        if not word or not ch:
            return word

        OurFlag = False
        for i in range(len(word)):
            if word[i] == ch:
                OurFlag = True
                break

        if not OurFlag:
            return word

        return word[i::-1] + word[i+1:]



word = "abcdefd"; ch = "d"
X = Solution()
print(X.reversePrefix1(word, ch))





