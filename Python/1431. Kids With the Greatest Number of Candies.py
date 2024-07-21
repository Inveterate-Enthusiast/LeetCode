# There are n kids with candies. You are given an integer array candies,
# where each candies[i] represents the number of candies the ith kid has,
# and an integer extraCandies, denoting the number of extra candies that you have.
#
# Return a boolean array result of length n,
# where result[i] is true if, after giving the ith kid all the extraCandies,
# they will have the greatest number of candies among all the kids, or false otherwise.
#
# Note that multiple kids can have the greatest number of candies.


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    OurResultArray = []
    OurMax = max(candies)
    for index in range(len(candies)):
        OurFlag = ((candies[index] + extraCandies) >= OurMax)
        OurResultArray.append(OurFlag)
    return OurResultArray

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))