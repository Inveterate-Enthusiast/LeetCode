# Table: Student
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | name        | varchar |
# | continent   | varchar |
# +-------------+---------+
# This table may contain duplicate rows.
# Each row of this table indicates the name of a student and the continent they came from.
#
#
# A school has students from Asia, Europe, and America.
#
# Write a solution to pivot the continent column in the Student table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output headers should be America, Asia, and Europe, respectively.
#
# The test cases are generated so that the student number from America is not less than either Asia or Europe.
import pandas as pd
import os
from pathlib import Path

def geography_report(student: pd.DataFrame) -> pd.DataFrame:
    continents = ["America", "Asia", "Europe"]
    if student.empty:
        return pd.DataFrame(columns=continents)

    grouped = student.groupby(by="continent", as_index=False).agg(students=("name", lambda x: list(x)))
    max_length = max(len(row) for row in grouped["students"])
    _dict = {continent: (x := ((sorted(*y, reverse=False)) if (y := grouped.loc[grouped["continent"] == continent, "students"].values.tolist()) else list())) + [None] * (max_length - len(x)) for continent in continents}
    return pd.DataFrame(_dict)

def geography_report1(student: pd.DataFrame) -> pd.DataFrame:
    continents = pd.DataFrame({
        "continent": ["America", "Asia", "Europe"]
    })
    student.sort_values(by="name", ascending=True, inplace=True)
    student = student.merge(right=continents, how="right", on="continent")
    student["order"] = student.groupby(by="continent", as_index=False).cumcount()
    return student.pivot(columns="continent", values="name", index="order").dropna(how="all")


path = Path(os.getcwd()) / "data" / "618. Students Report By Geography.xlsx"
student = pd.read_excel(path)
print(geography_report1(student))
