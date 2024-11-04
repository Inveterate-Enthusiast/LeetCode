# Table: students
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | student_id  | int      |
# | name        | varchar  |
# | major       | varchar  |
# +-------------+----------+
# student_id is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the student ID, student name, and their major.
# Table: courses
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | course_id   | int      |
# | name        | varchar  |
# | credits     | int      |
# | major       | varchar  |
# +-------------+----------+
# course_id is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the course ID, course name, the number of credits for the course, and the major it belongs to.
# Table: enrollments
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | student_id  | int      |
# | course_id   | int      |
# | semester    | varchar  |
# | grade       | varchar  |
# +-------------+----------+
# (student_id, course_id, semester) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the student ID, course ID, semester, and grade received.
# Write a solution to find the students who have taken all courses offered in their major and have achieved a grade of A in all these courses.
#
# Return the result table ordered by student_id in ascending order.

import pandas as pd
import numpy as np

def find_top_scoring_students(enrollments: pd.DataFrame, students: pd.DataFrame, courses: pd.DataFrame) -> pd.DataFrame:
    A = "A"
    merged = pd.merge(
        left=students,
        right=courses,
        how="left",
        on="major"
    )
    merged_2 = pd.merge(
        left=merged,
        right=enrollments,
        how="left",
        on=["student_id", "course_id"]
    )
    merged_2["check"] = np.where(merged_2["grade"] == A, 0, 1)
    grouped = merged_2.groupby(by="student_id", as_index=False).agg(our_sum=("check", "sum"))
    return grouped.loc[grouped["our_sum"] == 0, ["student_id"]].sort_values(by="student_id", ascending=True)