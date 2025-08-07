# You are given a string num representing a large integer. An integer is good if it meets the following conditions:
#
# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.
#
# Note:
#
# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.

from collections import defaultdict

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        our_dict = defaultdict(int)
        result = float("-inf")
        limit = 3
        for i in range(len(num)):
            our_dict[num[i]] += 1
            if our_dict[num[i]] == limit:
                result = max(result, int(num[i]))

            if i >= 2:
                our_dict[num[i - (limit - 1)]] -= 1
                if our_dict[num[i - (limit - 1)]] == 0: our_dict.pop(num[i - (limit - 1)])

        return (str(result) * limit) if result != float("-inf") else str()

num = "0006777133339"
x = Solution()
print(x.largestGoodInteger(num))