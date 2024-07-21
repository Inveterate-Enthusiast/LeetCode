# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

def maxArea1(height: list[int]) -> int:
    leftIndex = 0
    rightIndex = (len(height)-1)
    OurResultAmount = 0
    while leftIndex <= rightIndex:
        while rightIndex >= leftIndex and height[rightIndex] < height[leftIndex]:
            OurCurrentAmount = (min(height[leftIndex], height[rightIndex])) * (rightIndex - leftIndex)
            OurResultAmount = max(OurResultAmount, OurCurrentAmount)
            rightIndex -= 1
        OurCurrentAmount = (min(height[leftIndex], height[rightIndex])) * (rightIndex - leftIndex)
        OurResultAmount = max(OurResultAmount, OurCurrentAmount)
        leftIndex += 1
    return OurResultAmount

V = [1,8,100,2,100,4,8,3,7]
print(maxArea1(V))