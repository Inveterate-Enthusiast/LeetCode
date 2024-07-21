# Given a 0-indexed n x n integer matrix grid,
# return the number of pairs (ri, cj) such that row ri and column cj are equal.
#
# A row and column pair is considered equal
# if they contain the same elements in the same order (i.e., an equal array).

def equalPairs1(grid: list[list[int]]) -> int: #Решение через строку - ключ хэша
    OurHashRow = {}
    OurResultCount = 0
    for row in grid:
        OurValue = str("-".join(map(str, row)))
        OurHashRow[OurValue] = OurHashRow.get(OurValue, 0) + 1
    for column in range(len(grid[0])):
        OurValue = str("-".join(map(str, [grid[i][column] for i in range(len(grid))] )))
        if OurValue in OurHashRow:
            OurResultCount = OurResultCount + OurHashRow[OurValue]
    return OurResultCount

def equalPairs2(grid: list[list[int]]) -> int: #Решение через кортеж - ключ хэша
    OurHashRow = {}
    OurResultCount = 0
    for row in grid:
        OurValue = tuple(row)
        OurHashRow[OurValue] = OurHashRow.get(OurValue, 0) + 1
    for columnIndex in range(len(grid[0])):
        OurValue = tuple([grid[i][columnIndex] for i in range(len(grid))])
        if OurValue in OurHashRow:
            OurResultCount += OurHashRow[OurValue]
    return OurResultCount

grid = [[1,11],[11,1]]
print(equalPairs2(grid))