# You are given an integer array nums.
# You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.

def canJump1(nums: list[int]) -> bool:
    OurJumpLen = 0
    for jumps in nums:
        if OurJumpLen < 0:
            return False
        if jumps > OurJumpLen:
            OurJumpLen = jumps
        OurJumpLen -= 1
    return True


nums = [0,2,3]
print(canJump1(nums))