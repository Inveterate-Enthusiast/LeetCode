# Write a solution to calculate and display the number of rows and columns of players.
#
# Return the result as an array:
#
# [number of rows, number of columns]
#
# The result format is in the following example.


import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ["student_id", "age"])


student_data= \
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

student_data = createDataframe(student_data)

print(getDataframeSize(student_data))