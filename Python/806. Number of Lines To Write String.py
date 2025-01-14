# You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase
# English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.
#
# You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s,
# write as many letters on the first line such that the total width does not exceed 100 pixels.
# Then, from where you stopped in s, continue writing as many letters as you can on the second line.
# Continue this process until you have written all of s.
#
# Return an array result of length 2 where:
#
# result[0] is the total number of lines.
# result[1] is the width of the last line in pixels.

from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        dict_alpha = dict()
        for index, i in enumerate(range(97, 122+1)):
            dict_alpha[chr(i)] = widths[index]

        rows = 0
        temp_sum = 0
        for i in range(len(s)):
            if (temp_sum + dict_alpha[s[i]]) > 100:
                rows += 1
                left = i
                temp_sum = 0
            temp_sum += dict_alpha[s[i]]
        else:
            rows = (rows + 1) if temp_sum else rows
        return [rows, temp_sum]

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
x = Solution()
print(x.numberOfLines(widths, s))