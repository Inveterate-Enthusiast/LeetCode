# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

from datetime import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        ddate = datetime.strptime(date, "%Y-%m-%d")
        return (ddate - datetime.strptime(f"{ddate.year}-01-01", "%Y-%m-%d")).days + 1

date = "2019-02-10"
x = Solution()
print(x.dayOfYear(date))