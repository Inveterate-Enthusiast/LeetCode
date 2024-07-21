# Table: Triangle
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# | y           | int  |
# | z           | int  |
# +-------------+------+
# In SQL, (x, y, z) is the primary key column for this table.
# Each row of this table contains the lengths of three line segments.

# Report for every three line segments whether they can form a triangle.
#
# Return the result table in any order.
import pandas as pd
import numpy as np

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = triangle[["x", "y", "z"]].apply(lambda x: "Yes" if ((x["x"] + x["y"]) > x["z"]) and ((x["x"] + x["z"]) > x["y"]) and ((x["z"] + x["y"]) > x["x"]) else "No", axis=1)
    return triangle

def triangle_judgement1(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = np.where(
        ((triangle["x"] + triangle["y"]) > (triangle["z"])) &
        ((triangle["z"] + triangle["y"]) > (triangle["x"])) &
        ((triangle["x"] + triangle["z"]) > (triangle["y"])),
        "Yes",
        "No"
    )
    return triangle

def triangle_judgement2(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = (((triangle["x"] + triangle["y"]) > (triangle["z"])) &
                            ((triangle["x"] + triangle["z"]) > (triangle["y"])) &
                            ((triangle["z"] + triangle["y"]) > (triangle["x"])))

    triangle["triangle"] = triangle["triangle"].map({
        True: "Yes",
        False: "No"
    })

    return triangle

Triangle = pd.DataFrame({
    "x": [13, 10],
    "y": [15, 20],
    "z": [30, 15]
})

print(triangle_judgement2(Triangle))