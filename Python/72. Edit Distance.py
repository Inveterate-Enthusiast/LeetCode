# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character

def minDistance1(word1: str, word2: str) -> int:
    Matrix = [[((i + j) if i*j==0 else 0) for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
    for rowIndex in range(1, len(Matrix)):
        for columnsIndex in range(1, len(Matrix[0])):
            if word1[rowIndex-1] == word2[columnsIndex-1]:
                Matrix[rowIndex][columnsIndex] = Matrix[rowIndex-1][columnsIndex-1]
            else:
                Matrix[rowIndex][columnsIndex] = 1 + min(
                    Matrix[rowIndex][columnsIndex-1],
                    Matrix[rowIndex-1][columnsIndex],
                    Matrix[rowIndex-1][columnsIndex-1]
                )
    return Matrix[len(word1)][len(word2)]

word1 = "horse"; word2 = "ros"
print(minDistance1(word1, word2))