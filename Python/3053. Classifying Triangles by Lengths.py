# Table: Triangles
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | A           | int  |
# | B           | int  |
# | C           | int  |
# +-------------+------+
# (A, B, C) is the primary key for this table.
# Each row include the lengths of each of a triangle's three sides.
# Write a query to find the type of triangle. Output one of the following for each row:
#
# Equilateral: It's a triangle with 3 sides of equal length.
# Isosceles: It's a triangle with 2 sides of equal length.
# Scalene: It's a triangle with 3 sides of differing lengths.
# Not A Triangle: The given values of A, B, and C don't form a triangle.
# Return the result table in any order.
import pandas as pd

def type_of_triangle(triangles: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame({
        "triangle_type": []
    })
    for index, row in triangles.iterrows():
        if row["A"] >= (row["B"] + row["C"]) or row["B"] >= (row["A"] + row["C"]) or row["C"] >= (row["A"] + row["B"]):
            result.loc[result.shape[0]] = "Not A Triangle"
        elif row["A"] == row["B"] == row["C"]:
            result.loc[result.shape[0]] = "Equilateral"
        elif row["A"] == row["B"] or row["B"] == row["C"] or row["A"] == row["C"]:
            result.loc[result.shape[0]] = "Isosceles"
        elif row["A"] != row["B"] != row["C"]:
            result.loc[result.shape[0]] = "Scalene"
    return result
