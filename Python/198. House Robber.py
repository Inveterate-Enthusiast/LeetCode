# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that
# adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

def rob1(nums: list[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = max(nums[i-1], (nums[i] + (nums[i-2] if (i-2) >= 0 else 0)))
    return nums[-1]

nums = [2,7,9,3,1]
print(rob1(nums))