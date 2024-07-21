# There is a biker going on a road trip.
# The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
#
# You are given an integer array gain of length n
# where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n).
# Return the highest altitude of a point.

def largestAltitude(gain: list[int]) -> int:
    OurPrefixAltitude = [0]
    OurHighestAltutede = OurPrefixAltitude[0]
    for index in range(len(gain)):
        OurPrefixAltitude.append(OurPrefixAltitude[index] + gain[index])
        OurHighestAltutede = OurPrefixAltitude[-1] if OurPrefixAltitude[-1] > OurHighestAltutede else OurHighestAltutede
    return OurHighestAltutede

OurGain = [-4,-3,-2,-1,4,3,2]
print(largestAltitude(OurGain))