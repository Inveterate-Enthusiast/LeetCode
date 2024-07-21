# Write a solution to rename the columns as follows:
#
# id to student_id
# first to first_name
# last to last_name
# age to age_in_years
# The result format is in the following example.

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={"id": "student_id", "first": "first_name", "last": "last_name", "age": "age_in_years"})
    return students

data = [
    [1, "Mason", "King", 6],
    [2, "Ava", "Wright", 6],
    [3, "Taylor", "Hall", 6],
    [4, "Georgia", "Thompson", 6],
    [5, "Thomas", "Moore", 6],
]

data = pd.DataFrame(data, columns= ["id", "first", "last", "age"])
print(renameColumns(data))