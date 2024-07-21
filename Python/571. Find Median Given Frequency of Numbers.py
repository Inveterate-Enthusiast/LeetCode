# Table: Numbers
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | num         | int  |
# | frequency   | int  |
# +-------------+------+
# num is the primary key (column with unique values) for this table.
# Each row of this table shows the frequency of a number in the database.
#
#
# The median is the value separating the higher half from the lower half of a data sample.
#
# Write a solution to report the median of all the numbers in the database after decompressing the Numbers table.
# Round the median to one decimal point.
import pandas as pd
import numpy as np
from pathlib import Path
import os

def median_frequency(numbers: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "median": [round(np.median(
        [row["num"] for index, row in numbers.iterrows() for i in range(row["frequency"])]
    ), 1)]
    })


path = Path(os.getcwd()) / "data" / "571. Find Median Given Frequency of Numbers.xlsx"
numbers = pd.read_excel(path)
print(median_frequency1(numbers))



