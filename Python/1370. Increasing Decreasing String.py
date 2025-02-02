# You are given a string s. Reorder the string using the following algorithm:
#
# Remove the smallest character from s and append it to the result.
# Remove the smallest character from s that is greater than the last appended character, and append it to the result.
# Repeat step 2 until no more characters can be removed.
# Remove the largest character from s and append it to the result.
# Remove the largest character from s that is smaller than the last appended character, and append it to the result.
# Repeat step 5 until no more characters can be removed.
# Repeat steps 1 through 6 until all characters from s have been removed.
# If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.
#
# Return the resulting string after reordering s using this algorithm.

from collections import defaultdict

class Solution:
    def clean_dict(self, d: dict) -> dict:
        to_clean = list()
        for key in d:
            d[key] -= 1
            if d[key] == 0: to_clean.append(key)

        for i in to_clean:
            del d[i]

        return d

    def sortString(self, s: str) -> str:
        result = list()
        our_dict = defaultdict(int)
        for char in sorted(s):
            our_dict[char] += 1

        while our_dict:
            if our_dict: result.extend(list(our_dict.keys()))
            our_dict = self.clean_dict(our_dict)
            if our_dict: result.extend(list(our_dict.keys())[::-1])
            our_dict = self.clean_dict(our_dict)

        return "".join(result)

s = "aaaabbbbcccc"
x = Solution()
print(x.sortString(s))