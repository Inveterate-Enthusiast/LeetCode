# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.



def maximalSquare1(matrix: list[list[str]]) -> int:
    OurResult = 0
    OurPrefRow = [0] * len(matrix[0])
    OurCurrentRow = OurPrefRow.copy()

    for indexRow in range(len(matrix)):
        for indexColumn in range(len(matrix[0])):
            if matrix[indexRow][indexColumn] != "0":
                OurCurrentRow[indexColumn] = 1 + min(
                    OurCurrentRow[indexColumn-1] if indexColumn > 0 else 0,
                    OurPrefRow[indexColumn-1] if indexColumn > 0 else 0,
                    OurPrefRow[indexColumn]
                )
                OurResult = max(OurResult, OurCurrentRow[indexColumn])

        OurPrefRow = OurCurrentRow
        OurCurrentRow = [0] * len(matrix[0])

    return OurResult**2

# Решение не правильное
def maximalSquare2(matrix: list[list[str]]) -> int:
    OurDP = [[0] * len(matrix[0]) for i in range(len(matrix))]

    for indexRow in range(len(matrix)):
        for indexColumn in range(len(matrix[0])):
            if indexRow == indexColumn == 0:
                OurDP[indexRow][indexColumn] = int(matrix[indexRow][indexColumn])
            elif indexRow == 0:
                OurDP[indexRow][indexColumn] = max(OurDP[indexRow][indexColumn-1], int(matrix[indexRow][indexColumn]))
            elif indexColumn == 0:
                OurDP[indexRow][indexColumn] = max(OurDP[indexRow-1][indexColumn], int(matrix[indexRow][indexColumn]))
            else:
                if (matrix[indexRow][indexColumn] != "0") and (matrix[indexRow-1][indexColumn] != "0") and (matrix[indexRow][indexColumn-1] != "0") and (matrix[indexRow-1][indexColumn-1] != "0"):
                    OurDP[indexRow][indexColumn] = 1 + min(
                        OurDP[indexRow][indexColumn-1],
                        OurDP[indexRow-1][indexColumn],
                        OurDP[indexRow-1][indexColumn-1]
                    )
                else:
                    OurDP[indexRow][indexColumn] = max(
                        OurDP[indexRow][indexColumn-1],
                        OurDP[indexRow-1][indexColumn],
                        OurDP[indexRow-1][indexColumn-1]
                    )

    return OurDP[-1][-1]**2

def maximalSquare3(matrix: list[list[str]]) -> int:
    OurDP = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    OurResult = 0

    for indexRow in range(len(matrix)):
        for indexColumn in range(len(matrix[0])):
            if indexRow == indexColumn == 0:
                OurDP[indexRow][indexColumn] = int(matrix[indexRow][indexColumn])
                OurResult = max(OurResult, OurDP[indexRow][indexColumn])
            else:
                if matrix[indexRow][indexColumn] != "0":
                    OurDP[indexRow][indexColumn] = 1 + min(
                        OurDP[indexRow][indexColumn-1] if indexColumn > 0 else 0,
                        OurDP[indexRow-1][indexColumn] if indexRow > 0 else 0,
                        OurDP[indexRow-1][indexColumn-1] if indexRow*indexColumn != 0 else 0
                    )
                    OurResult = max(OurResult, OurDP[indexRow][indexColumn])

    return OurResult**2


matrix = [["1"]]
print(maximalSquare3(matrix))