# Write a solution to display the first 3 rows of this DataFrame.

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:3]

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
print(selectFirstRows(student_data))