# Table: Enrollments
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | course_id     | int     |
# | grade         | int     |
# +---------------+---------+
# (student_id, course_id) is the primary key (combination of columns with unique values) of this table.
# grade is never NULL.
#
#
# Write a solution to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id.
#
# Return the result table ordered by student_id in ascending order.
import pandas as pd

def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:
    enrollments.sort_values(by=["grade", "course_id"], ascending=[False, True], inplace=True)
    return enrollments.drop_duplicates(subset="student_id", keep="first").sort_values(by="student_id", ascending=True)

def highest_grade1(enrollments: pd.DataFrame) -> pd.DataFrame:
    enrollments["rank_of_grade"] = enrollments.groupby(by="student_id")["grade"].rank(method="dense", ascending=False)
    enrollments["rank_of_course"] = enrollments.groupby(by=["student_id", "grade"])["course_id"].rank(method="dense", ascending=True)
    print(enrollments)
    return enrollments.loc[
        (enrollments["rank_of_grade"] == 1)
        &
        (enrollments["rank_of_course"] == 1),
        ["student_id", "course_id", "grade"]
    ].sort_values(by="student_id", ascending=True)
