# Given an array of integers arr,
# return true if the number of occurrences of each value in the array is unique or false otherwise.

def uniqueOccurrences1(arr: list[int]) -> bool:
    OurDict = {}
    OurSet = set()
    OurList = []
    for value in arr:
        if value not in OurDict:
            OurDict[value] = 1
        else:
            OurDict[value] += 1
    for index, value in OurDict.items():
        OurSet.add(value)
        OurList.append(value)
    return len(OurSet) == len(OurList)


def uniqueOccurrences2(arr: list[int]) -> bool:
    OurDict ={}
    for value in arr:
        OurDict[value] = OurDict.get(value, 0) + 1
    return (len(set(OurDict.values()))) == (len(OurDict.values()))


arr = [1,2,2,1,1,3]
print(uniqueOccurrences2(arr))