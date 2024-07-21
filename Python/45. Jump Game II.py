# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

def jump1(nums: list[int]) -> int:
    OurJumpLen = [float("inf")] * len(nums)
    OurJumpLen[0] = 0
    for i in range(len(nums)):
        for j in range(1, ((nums[i]+1) if (i + nums[i]) < (len(nums)-1) else (len(nums)-i))):
            OurJumpLen[i+j] = min(OurJumpLen[i] + 1, OurJumpLen[i+j])
    return OurJumpLen[len(nums)-1]

nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(jump1(nums))