# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at
# a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
#
# Note that you do not have any change in hand at first.
#
# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer
# with the correct change, or false otherwise.
from typing import List
from collections import deque
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        our_dict = {
            5: 0,
            10: 0,
            20: 0
        }
        for bill in bills:
            if bill == 5:
                our_dict[5] += 1
            else:
                temp_bill = (bill-5)
                our_dict[bill] += 1
                for cur_max in reversed(our_dict.keys()):
                    while our_dict[cur_max] and temp_bill and temp_bill >= cur_max:
                        temp_bill -= cur_max; our_dict[cur_max] -= 1

                if temp_bill: return False
        return True

bills = [5,5,5,10,20]
x = Solution()
print(x.lemonadeChange(bills))