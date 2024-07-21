# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


def generateParenthesis1(n: int) -> list[str]:
    OurResultList = []
    left = right = 0
    CurList = [(left, right, '')]
    while CurList:
        left, right, TempStr = CurList.pop()
        if len(TempStr) == 2 * n:
            OurResultList.append(TempStr)
        if left < n:
            CurList.append((left + 1, right, TempStr + '('))
        if right < left:
            CurList.append((left, right + 1, TempStr + ')'))
    return OurResultList


OurN = 2
print(generateParenthesis1(OurN))


# Аналогичный подход для поиска всех возможных перестановок множества (длина комбинации равна длине множества)
OurV = [10,5] # гарантируется, что все элементы разные
def generatePermutation1(lst: list) -> list[str]:
    if len(lst) < 2:
        return lst
    OurFac = 1
    for i in range(2, len(lst) + 1):
        OurFac *= i
    OurResult = [[None for _ in range(len(lst))] for _ in range(OurFac)]
    for indexDigit in range(len(lst)):
        t = OurFac // len(lst)
        i = indexDigit; j = 0
        for index in range(len(OurResult)):
            if t == 0:
                t = OurFac // len(lst)
                j += 1
                i = (indexDigit + j)%len(lst)
            OurResult[index][i] = lst[indexDigit]
            t -= 1

    return OurResult

print(generatePermutation1(OurV))

def generateSubSet1(arr: list, subarr: list) -> list[str]:
    lenSubArr, lenArr = len(subarr), len(arr)
    Matrix = [[0] * (lenArr + 1) for _ in range(lenSubArr + 1)]

    for j in range(lenArr + 1):
        Matrix[0][j] = 1

    for i in range(1, lenSubArr + 1):
        for j in range(1, lenArr + 1):
            if subarr[i - 1] == arr[j - 1]:
                Matrix[i][j] = Matrix[i - 1][j - 1] + Matrix[i][j - 1]
            else:
                Matrix[i][j] = Matrix[i][j - 1]

    return Matrix[lenSubArr][lenArr]

OurLst = [1,2,3]
OurSub = [1,1,1]
print(generateSubSet1(OurLst, OurSub))