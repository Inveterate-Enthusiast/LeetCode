# Table: Point
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# +-------------+------+
# In SQL, x is the primary key column for this table.
# Each row of this table indicates the position of a point on the X-axis.

# Find the shortest distance between any two points from the Point table.

import pandas as pd
from pathlib import Path

def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    point["shortest"] = point["x"].sort_values(inplace=False, na_position="first").diff(periods=(1)).abs()
    point.dropna(subset="shortest", inplace=True)
    return point[point["shortest"] == point["shortest"].min()][["shortest"]].drop_duplicates(keep="first", inplace=False)

def shortest_distance1(point: pd.DataFrame) -> pd.DataFrame:
    point.sort_values(
        by="x",
        inplace=True,
        na_position="first"
    )
    return pd.DataFrame({
        "shortest": [point["x"].diff(periods=1).min()]
    })

path = Path(__file__).parent / "data" / "613. Point.xlsx"
Point = pd.read_excel(path)
print(shortest_distance(Point))