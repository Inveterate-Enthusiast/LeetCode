# Table: Point2D
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# | y           | int  |
# +-------------+------+
# (x, y) is the primary key column (combination of columns with unique values) for this table.
# Each row of this table indicates the position of a point on the X-Y plane.
#
#
# The distance between two points p1(x1, y1) and p2(x2, y2) is sqrt((x2 - x1)2 + (y2 - y1)2).
#
# Write a solution to report the shortest distance between any two points from the Point2D table.
# Round the distance to two decimal points.
import pandas as pd
import os
from pathlib import Path

def shortest_distance(point2_d: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=point2_d,
        right=point2_d,
        suffixes=("_left", "_right"),
        how="cross"
    )
    merged.drop(index= merged[(merged["x_left"] == merged["x_right"]) & (merged["y_left"] == merged["y_right"])].index,inplace=True)
    merged["path"] = ((merged["x_right"] - merged["x_left"])**2 + (merged["y_right"] - merged["y_left"])**2)**(1/2)
    return pd.DataFrame({
        "shortest": [(round(merged["path"].min(), 2))]
    })

path = Path(os.getcwd()) / "data" / "612. Shortest Distance in a Plane.xlsx"
point2_d = pd.read_excel(path)
print(shortest_distance(point2_d))