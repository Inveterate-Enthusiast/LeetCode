# Table: students
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | student_id  | int      |
# | name        | varchar  |
# | major       | varchar  |
# +-------------+----------+
# student_id is the primary key for this table.
# Each row contains the student ID, student name, and their major.
# Table: courses
#
# +-------------+-------------------+
# | Column Name | Type              |
# +-------------+-------------------+
# | course_id   | int               |
# | name        | varchar           |
# | credits     | int               |
# | major       | varchar           |
# | mandatory   | enum              |
# +-------------+-------------------+
# course_id is the primary key for this table.
# mandatory is an enum type of ('Yes', 'No').
# Each row contains the course ID, course name, credits, major it belongs to, and whether the course is mandatory.
# Table: enrollments
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | student_id  | int      |
# | course_id   | int      |
# | semester    | varchar  |
# | grade       | varchar  |
# | GPA         | decimal  |
# +-------------+----------+
# (student_id, course_id, semester) is the primary key (combination of columns with unique values) for this table.
# Each row contains the student ID, course ID, semester, and grade received.
# Write a solution to find the students who meet the following criteria:
#
# Have taken all mandatory courses and at least two elective courses offered in their major.
# Achieved a grade of A in all mandatory courses and at least B in elective courses.
# Maintained an average GPA of at least 2.5 across all their courses (including those outside their major).
# Return the result table ordered by student_id in ascending order.


import pandas as pd
import numpy as np

def find_top_scoring_students(students: pd.DataFrame, courses: pd.DataFrame, enrollments: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=students,
        right=courses.rename(columns={"name": "course"}),
        how="inner",
        on="major"
    )
    merged = pd.merge(
        left=merged,
        right=enrollments,
        how="left",
        on=["student_id", "course_id"]
    )
    merged["bool_mandatory"] = np.where(
        (merged["mandatory"] == "Yes")
        &
        ((merged["grade"].isna()) | (merged["grade"] > "A")),
        1,
        0
    )
    merged["bool_mandatory"] = merged.groupby(by="student_id", as_index=False)["bool_mandatory"].transform("sum")
    merged = merged.loc[merged["bool_mandatory"] == 0].copy()
    merged["bool_elective"] = np.where(
        (merged["mandatory"] == "No")
        &
        ((~merged["grade"].isna()) & (merged["grade"] <= "B")),
        1,
        0
    )
    merged["bool_elective"] = merged.groupby(by="student_id", as_index=False)["bool_elective"].transform("sum")
    merged = merged.loc[merged["bool_elective"] >= 2]
    merged = pd.merge(
        left=merged[["student_id"]].drop_duplicates(keep="first"),
        right=enrollments,
        how="inner",
        on="student_id"
    )
    grouped = merged.groupby(by="student_id", as_index=False).agg(avg_GPA=("GPA", "mean"))
    return grouped.loc[grouped["avg_GPA"] >= 2.5, ["student_id"]].sort_values(by="student_id", ascending=True)