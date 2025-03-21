# You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.
#
# Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.

from collections import defaultdict

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        our_dict = defaultdict(lambda: [0, 0])
        for i in target:
            our_dict[i][0] += 1

        for i in s:
            if i in our_dict:
                our_dict[i][1] += 1

        result = float("inf")
        for key, value in our_dict.items():
            if value[0] > value[1]:
                return 0
            result = min(result, (value[1] // value[0]))
        return 0 if result == float("inf") else result

    def rearrangeCharacters1(self, s: str, target: str) -> int:
        dict_target = defaultdict(int)
        dict_s = defaultdict(int)
        for i in target:
            dict_target[i] += 1

        for i in s:
            if i in dict_target:
                dict_s[i] += 1

        result = float("inf")
        for key, value in dict_target.items():
            if not key in dict_s or value > dict_s[key]:
                return 0
            result = min(result, (dict_s[key] // value))
        return 0 if result == float("inf") else result

s = "codecodecodecode"
target = "codecode"
x = Solution()
print(x.rearrangeCharacters1(s,target))