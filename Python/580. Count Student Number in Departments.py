# Table: Student
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | student_id   | int     |
# | student_name | varchar |
# | gender       | varchar |
# | dept_id      | int     |
# +--------------+---------+
# student_id is the primary key (column with unique values) for this table.
# dept_id is a foreign key (reference column) to dept_id in the Department tables.
# Each row of this table indicates the name of a student, their gender, and the id of their department.
#
#
# Table: Department
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | dept_id     | int     |
# | dept_name   | varchar |
# +-------------+---------+
# dept_id is the primary key (column with unique values) for this table.
# Each row of this table contains the id and the name of a department.
#
#
# Write a solution to report the respective department name and number of students majoring
# in each department for all departments in the Department table (even ones with no current students).
#
# Return the result table ordered by student_number in descending order. In case of a tie, order them by dept_name alphabetically.
import pandas as pd

def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    grouped = student.groupby(by="dept_id", as_index=False).agg(student_number=("student_id", "nunique"))
    return pd.merge(
        left=department,
        right=grouped,
        on="dept_id",
        how="left"
    ).fillna(0).sort_values(by=["student_number", "dept_name"], ascending=[False, True]).loc[:, ["dept_name", "student_number"]]

