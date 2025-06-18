# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
#
# Return the sorted string. If there are multiple answers, return any of them.

from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        our_dict = defaultdict(int)
        for i in s:
            our_dict[i] += 1

        temp_list = sorted([(l, freq) for l, freq in our_dict.items()], reverse=True, key=lambda x: x[1])
        result = str()
        for l, freq in temp_list:
            result += (l * freq)

        return result

    def frequencySort1(self, s: str) -> str:
        our_dict = defaultdict(int)
        for i in s:
            our_dict[i] += 1

        max_freq = max(our_dict.values())
        temp_list = [list() for _ in range(max_freq + 1)]
        for l, freq in our_dict.items():
            temp_list[freq].append(l)

        result = str()
        for index_pack in range(len(temp_list)-1, 0, -1):
            for l in temp_list[index_pack]:
                result += (l * index_pack)
        return result

s = "tree"
x = Solution()
print(x.frequencySort1(s))