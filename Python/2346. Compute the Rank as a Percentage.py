# Table: Students
#
# +---------------+------+
# | Column Name   | Type |
# +---------------+------+
# | student_id    | int  |
# | department_id | int  |
# | mark          | int  |
# +---------------+------+
# student_id contains unique values.
# Each row of this table indicates a student's ID, the ID of the department in which the student enrolled, and their mark in the exam.
#
#
# Write a solution to report the rank of each student in their department as a percentage,
# where the rank as a percentage is computed using the following formula: (student_rank_in_the_department - 1) * 100 /
# (the_number_of_students_in_the_department - 1). The percentage should be rounded to 2 decimal places.
# student_rank_in_the_department is determined by descending mark, such that the student with the highest mark is rank 1.
# If two students get the same mark, they also get the same rank.
#
# Return the result table in any order.
import pandas as pd
import numpy as np

def compute_rating(students: pd.DataFrame) -> pd.DataFrame:
    students["rank"] = students.groupby(by="department_id", as_index=False)["mark"].rank(method="min", ascending=False)
    students["num"] = students.groupby(by="department_id", as_index=False)["student_id"].transform("nunique")
    students["percentage"] = np.where((students["num"] - 1) > 0, ((students["rank"] - 1) * 100 / (students["num"] - 1) +1e-9).round(2), 0)
    return students[["student_id", "department_id", "percentage"]]


