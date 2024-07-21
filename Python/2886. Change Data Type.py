# Write a solution to correct the errors:
#
# The grade column is stored as floats, convert it to integers.
#
# The result format is in the following example.

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students

data = {
    "student_id": [1, 2],
    "name": ["Ave", "Kate"],
    "age": [6, 15],
    "grade": [float(73), float(87)]
}
data = pd.DataFrame(data)
print(changeDatatype(data))