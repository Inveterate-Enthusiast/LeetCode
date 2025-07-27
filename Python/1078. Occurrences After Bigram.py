# Given two strings first and second, consider occurrences in some text of the form "first second third",
# where second comes immediately after first, and third comes immediately after second.
#
# Return an array of all the words third for each occurrence of "first second third".

from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = list()

        word_list = text.split(" ")
        n = len(word_list)
        if n < 3:
            return list()

        for i in range(2, n):
            if word_list[i-2] == first and word_list[i-1] == second:
                result.append(word_list[i])

        return result

text = "we will we will rock you"
first = "we"
second = "will"
x = Solution()
print(x.findOcurrences(text, first, second))
