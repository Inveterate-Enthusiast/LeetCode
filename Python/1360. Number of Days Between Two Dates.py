# Write a program to count the number of days between two dates.
#
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

import pandas as pd
from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date11 = pd.to_datetime(arg=date1, format="%Y-%m-%d")
        date22 = pd.to_datetime(arg=date2, format="%Y-%m-%d")
        return (date22 - date11).days

    def daysBetweenDates1(self, date1: str, date2: str) -> int:
        date11 = datetime.strptime(date1, "%Y-%m-%d").date()
        date22 = datetime.strptime(date2, "%Y-%m-%d").date()
        return abs(date22 - date11).days

date1 = "2019-06-29"
date2 = "2019-06-30"
x = Solution()
print(x.daysBetweenDates1(date1, date2))