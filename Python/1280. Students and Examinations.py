# Table: Students
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | student_name  | varchar |
# +---------------+---------+
# student_id is the primary key (column with unique values) for this table.
# Each row of this table contains the ID and the name of one student in the school.

# Table: Subjects
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | subject_name | varchar |
# +--------------+---------+
# subject_name is the primary key (column with unique values) for this table.
# Each row of this table contains the name of one subject in the school.

# Table: Examinations
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | student_id   | int     |
# | subject_name | varchar |
# +--------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each student from the Students table takes every course from the Subjects table.
# Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

# Write a solution to find the number of times each student attended each exam.
#
# Return the result table ordered by student_id and subject_name.
import pandas as pd
from pathlib import Path
import os

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=students,
        right=subjects,
        how="cross"
    )
    grouped = examinations.groupby(by=["student_id", "subject_name"], as_index=False).size().rename(columns={"size": "attended_exams"})
    ansDF = merged.merge(right=grouped,
                    how="left",
                    on=["student_id", "subject_name"]).sort_values(by=["student_id", "subject_name"])
    ansDF["attended_exams"] = ansDF["attended_exams"].fillna(0).astype(int)
    return ansDF[["student_id", "student_name", "subject_name", "attended_exams"]]



path = Path(os.getcwd()) / "data" / "1280. Students and Examinations.xlsx"
students = pd.read_excel(path, sheet_name="Students")
subjects = pd.read_excel(path, sheet_name="Subjects")
examinations = pd.read_excel(path, sheet_name="Examinations")
print(students_and_examinations1(students, subjects, examinations))


