# Table: Student
#
# +---------------------+---------+
# | Column Name         | Type    |
# +---------------------+---------+
# | student_id          | int     |
# | student_name        | varchar |
# +---------------------+---------+
# student_id is the primary key (column with unique values) for this table.
# student_name is the name of the student.
#
#
# Table: Exam
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | exam_id       | int     |
# | student_id    | int     |
# | score         | int     |
# +---------------+---------+
# (exam_id, student_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates that the student with student_id had a score points in the exam with id exam_id.
#
#
# A quiet student is the one who took at least one exam and did not score the highest or the lowest score.
#
# Write a solution to report the students (student_id, student_name) being quiet in all exams. Do not return the student who has never taken any exam.
#
# Return the result table ordered by student_id.


import pandas as pd
import numpy as np

def find_quiet_students(student: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=student,
        right=exam,
        how="inner",
        on="student_id"
    )
    merged["max"] = merged.groupby(by="exam_id", as_index=False)["score"].transform("max")
    merged["min"] = merged.groupby(by="exam_id", as_index=False)["score"].transform("min")
    merged["bool"] = np.where(
        (merged["score"] > merged["min"])
        &
        (merged["score"] < merged["max"]),
        0,
        1
    )
    grouped = merged.groupby(by=["student_id", "student_name"], as_index=False).agg(sum=("bool", "sum"))
    return grouped.loc[grouped["sum"] == 0, ["student_id", "student_name"]].sort_values(by="student_id", ascending=True)
