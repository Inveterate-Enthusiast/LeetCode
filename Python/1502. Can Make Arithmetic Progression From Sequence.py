# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
#
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
import math
def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    mid = math.floor(len(arr)/2)
    pivot = arr[mid]
    lessArr = [arr[i] for i in range(len(arr)) if i != mid and arr[i] <= pivot]
    greaterArr = [arr[i] for i in range(len(arr)) if i != mid and arr[i] > pivot]
    return quick_sort(lessArr) + [pivot] + quick_sort(greaterArr)

def canMakeArithmeticProgression1(arr: list[int]) -> bool:
    if len(arr) <= 2:
        return True
    arr = quick_sort(arr)
    for index in range(len(arr)):
        if index == 0:
            Dif = arr[index+1] - arr[index]
        else:
            if (arr[index] - arr[index-1] != Dif):
                return False
    return True

def canMakeArithmeticProgression2(arr: list[int]) -> bool:
    arr = sorted(arr, reverse=False)
    for index in range(len(arr)):
        if index == 0:
            Dif = arr[index+1] - arr[index]
        else:
            if (arr[index] - arr[index-1] != Dif):
                return False
    return True


arr = [3,5,1]
print(canMakeArithmeticProgression2(arr))