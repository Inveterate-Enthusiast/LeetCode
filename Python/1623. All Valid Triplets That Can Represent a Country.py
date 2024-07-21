# Table: SchoolA
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | student_name  | varchar |
# +---------------+---------+
# student_id is the column with unique values for this table.
# Each row of this table contains the name and the id of a student in school A.
# All student_name are distinct.
#
#
# Table: SchoolB
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | student_name  | varchar |
# +---------------+---------+
# student_id is the column with unique values for this table.
# Each row of this table contains the name and the id of a student in school B.
# All student_name are distinct.
#
#
# Table: SchoolC
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | student_name  | varchar |
# +---------------+---------+
# student_id is the column with unique values for this table.
# Each row of this table contains the name and the id of a student in school C.
# All student_name are distinct.
#
#
# There is a country with three schools, where each student is enrolled in exactly one school. The country is joining a competition and wants to select one student from each school to represent the country such that:
#
# member_A is selected from SchoolA,
# member_B is selected from SchoolB,
# member_C is selected from SchoolC, and
# The selected students' names and IDs are pairwise distinct (i.e. no two students share the same name, and no two students share the same ID).
# Write a solution to find all the possible triplets representing the country under the given constraints.
#
# Return the result table in any order.
import pandas as pd

def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:
    school_a.rename(columns={"student_id": "id_a", "student_name": "member_A"}, inplace=True)
    school_b.rename(columns={"student_id": "id_b", "student_name": "member_B"}, inplace=True)
    school_c.rename(columns={"student_id": "id_c", "student_name": "member_C"}, inplace=True)
    joined = (school_a
              .join(other=school_b, how="cross")
              .join(other=school_c, how="cross")
              )
    print(joined)
    return joined.loc[
        (joined["id_a"] != joined["id_b"]) &
        (joined["id_a"] != joined["id_c"]) &
        (joined["id_b"] != joined["id_c"]) &
        (joined["member_A"] != joined["member_B"]) &
        (joined["member_A"] != joined["member_C"]) &
        (joined["member_B"] != joined["member_C"]),
        ["member_A", "member_B", "member_C"]
    ]

