# Table: Points
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | x_value       | int     |
# | y_value       | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# Each point is represented as a 2D coordinate (x_value, y_value).
#
#
# Write a solution to report all possible axis-aligned rectangles with a non-zero area that can be formed by any two points from the Points table.
#
# Each row in the result should contain three columns (p1, p2, area) where:
#
# p1 and p2 are the id's of the two points that determine the opposite corners of a rectangle.
# area is the area of the rectangle and must be non-zero.
# Return the result table ordered by area in descending order.
# If there is a tie, order them by p1 in ascending order. If there is still a tie, order them by p2 in ascending order.
import pandas as pd
from pathlib import Path
import os

def rectangles_area(points: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=points,
        right=points,
        how="cross",
        suffixes=("_p1", "_p2")
    ).query("(x_value_p1 != x_value_p2) & (y_value_p1 != y_value_p2) & (id_p1 < id_p2)")
    merged["area"] = abs(merged["x_value_p1"] - merged["x_value_p2"]) * abs(merged["y_value_p1"] - merged["y_value_p2"])
    return (merged
            .rename(columns={"id_p1": "p1", "id_p2": "p2"})
            .loc[:,["p1", "p2", "area"]]
            .sort_values(by=["area", "p1", "p2"], ascending=[False, True, True]))

points = pd.read_excel(Path(os.getcwd()) / "data" / "1459. Rectangles Area.xlsx")
print(rectangles_area(points))