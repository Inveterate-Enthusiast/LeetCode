# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"
        dict_word = defaultdict(int)
        dict_text = defaultdict(int)
        for w in word:
            dict_word[w] += 1

        for w in text:
            dict_text[w] += 1

        result = 0
        while dict_text:
            for k, v in dict_word.items():
                if (not k in dict_text) or dict_text[k] < v:
                    return result
                dict_text[k] -= v
                if dict_text[k] == 0: dict_text.pop(k)
            result += 1
        return result

text = "nlaebolko"
x = Solution()
print(x.maxNumberOfBalloons(text))