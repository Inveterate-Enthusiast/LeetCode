# Write a solution to select the name and age of the student with student_id = 101.
#
# The result format is in the following example.

import pandas as pd


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ["student_id", "age"])


student_data= \
[
  [101, 15],
  [201, 11],
  [301, 11],
  [401, 20]
]

student_data = createDataframe(student_data)


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101]

    # return students.loc[students['student_id'] == 101]

print(selectData(student_data))