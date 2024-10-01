# Table: Data
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | first_col   | int  |
# | second_col  | int  |
# +-------------+------+
# This table may contain duplicate rows.
#
#
# Write a solution to independently:
#
# order first_col in ascending order.
# order second_col in descending order.
import pandas as pd
from pathlib import Path
import os

def order_two_columns(data: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "first_col": data["first_col"].sort_values(ascending=True).tolist(),
        "second_col": data["second_col"].sort_values(ascending=False).tolist()
    })

def order_two_columns1(data: pd.DataFrame) -> pd.DataFrame:
    return pd.concat(
        [data[["first_col"]].sort_values(by="first_col", ascending=True).reset_index(drop=True),
        data[["second_col"]].sort_values(by="second_col", ascending=False).reset_index(drop=True)],
        axis=1
    )

data = pd.read_excel(Path(os.getcwd()) / "data" / "2159. Order Two Columns Independently.xlsx")
print(order_two_columns1(data))