# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
#
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

def findGCD(nums: list[int]) -> int:
    if len(nums) == 2 and nums[0] == nums[1]:
        return nums[0]
    OurMax = max(nums)
    OurMin = min(nums)
    while OurMax > 0 and OurMin > 0 and OurMax != OurMin:
        GCD = (OurMax - OurMin) if OurMax > OurMin else (OurMin - OurMax)
        if OurMax % GCD == 0 and OurMin % GCD == 0:
            break
        else:
            OurMax, OurMin = (OurMax - OurMin if OurMax > OurMin else OurMax), \
                (OurMin - OurMax if OurMin > OurMax else OurMin)
    else:
        if OurMax == OurMin:
            GCD = OurMax
    return GCD

V = [2, 2, 2]
print(findGCD(V))
