# Table: Heights
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | height      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table, and it is guaranteed to be in sequential order.
# Each row of this table contains an id and height.
# Write a solution to calculate the amount of rainwater can be trapped between the bars in the landscape, considering that each bar has a width of 1 unit.
#
# Return the result table in any order.
#
# The result format is in the following example.


import pandas as pd
import numpy as np
from pathlib import Path
import os

def calculate_trapped_rain_water(heights: pd.DataFrame) -> pd.DataFrame:
    result = np.minimum(heights["height"].cummax(), heights["height"][::-1].cummax())
    return pd.DataFrame({
        "total_trapped_water": [np.maximum(result - heights["height"], 0).sum()]
    })


heights = pd.read_excel(Path(os.getcwd()) / "data" / "3061. Calculate Trapping Rain Water.xlsx")
print(calculate_trapped_rain_water(heights))