# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
#
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        our_min, our_max = min(salary), max(salary)
        result = [i for i in salary if (i != our_min) and (i != our_max)]
        return sum(result) / len(result)

salary = [4000,3000,1000,2000]
x = Solution()
print(x.average(salary))