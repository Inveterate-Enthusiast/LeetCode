# Alice and Bob have a different total number of candies.
# You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i]
# is the number of candies of the ith box of candy that Alice has and bobSizes[j]
# is the number of candies of the jth box of candy that Bob has.
#
# Since they are friends, they would like to exchange one candy box each so that after the exchange,
# they both have the same total amount of candy. The total amount of candy a person has is the sum of the number
# of candies in each box they have.
#
# Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange,
# and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers,
# you may return any one of them. It is guaranteed that at least one answer exists.

from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice, sum_bob = 0, 0
        set_bob = set()
        for i in aliceSizes:
            sum_alice += i
        for i in bobSizes:
            sum_bob += i
            set_bob.add(i)
        dif = sum_alice - sum_bob
        for i in aliceSizes:
            if (j := (i - (dif / 2))) in set_bob:
                return [i, j]

        return [0, 0]





aliceSizes = [20,35,22,6,13]
bobSizes = [31,57]
x = Solution()
print(x.fairCandySwap(aliceSizes, bobSizes))