# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome1(x: int) -> bool:
    x = list(str(x))
    left, right = 0, len(x)-1
    while left <= right:
        if x[left] != x[right]:
            return False
        left += 1; right -= 1
    return True

def isPalindrome2(x:int) -> bool:
    x = str(x)
    return x == x[::-1]

x = -121
print(isPalindrome1(x))