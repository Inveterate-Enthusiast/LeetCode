# Given a string s,
# check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

def repeatedSubstringPattern1(s: str) -> bool:
    if len(s) < 2:
        return False

    if s[:(len(s)//2)] == s[(len(s)//2):]:
        return True
    else:
        OurFrefFun = [0] * len(s)
        i, j = 1, 0
        while i < len(s):
            if s[i] == s[j]:
                OurFrefFun[i] = j+1
                i += 1; j += 1
            else:
                if j != 0:
                    j = OurFrefFun[j-1]
                else:
                    i += 1
    return (OurFrefFun[len(s) - 1] != 0) and (((len(s)) % ((len(s)) - OurFrefFun[(len(s) - 1)])) == 0)

def repeatedSubstringPattern2(s: str) -> bool: # гениальное решение от пользователя LeetCode
    ss = (s*2)[1:-1]
    return ss.find(s) != -1


s = "abac"
print(repeatedSubstringPattern2(s))