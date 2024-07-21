# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

def rob1(nums: list[int]) -> int:
    if len(nums) <= 3:
        return max(nums)

    def TempDef(nums):
        Temp1 = Temp2 = 0
        for Money in nums:
            Temp = max(Money + Temp1, Temp2)
            Temp1 = Temp2
            Temp2 = Temp
        return max(Temp1, Temp2)

    return max(TempDef(nums[1:]), TempDef(nums[:-1]))


nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(rob1(nums))
