# Table: Logs
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | num         | varchar |
# +-------------+---------+
# In SQL, id is the primary key for this table.
# id is an autoincrement column.
#
#
# Find all numbers that appear at least three times consecutively.
#
# Return the result table in any order.
import pandas as pd
import os
from pathlib import Path

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs["our_count"] = pd.Series(dtype="int")
    logs.sort_values(by="id", ascending=True, inplace=True)
    prevId = prevNum = prevCount = None
    for index, row in logs.iterrows():
        if (row["id"] - 1) == prevId and row["num"] == prevNum:
            logs.loc[index, "our_count"] = prevCount + 1
        else:
            logs.loc[index, "our_count"] = 1
        prevId, prevNum, prevCount = row["id"], row["num"], logs.loc[index, "our_count"]

    grouped = (logs.groupby(by="num", as_index=False)
               .agg(our_count=("our_count", "max"))
               .rename(columns={"num": "ConsecutiveNums"}))
    return grouped.loc[grouped["our_count"] >= 3, ["ConsecutiveNums"]]

def consecutive_numbers1(logs: pd.DataFrame) -> pd.DataFrame: # работает, но только у нас id сломанные, нужно ориентироваться по ним
    logs["our_count"] = logs["num"].rolling(window=3, min_periods=3).var()
    print(logs)
    return pd.DataFrame({
        "ConsecutiveNums": logs.loc[logs["our_count"] == 0, "num"].unique()
    })


def consecutive_numbers2(logs: pd.DataFrame) -> pd.DataFrame:
    logs.sort_values(by=['id'], inplace=True)

    logs = logs[(logs.num == logs.num.shift(1)) &
                (logs.num == logs.num.shift(2)) &
                (logs.id == logs.id.shift(1) + 1) &
                (logs.id == logs.id.shift(2) + 2)
                ].drop_duplicates('num')

    return logs.iloc[:, [1]].rename(columns={'num': 'ConsecutiveNums'})

path = Path(os.getcwd()) / "data" / "180. Consecutive Numbers.xlsx"
logs = pd.read_excel(path, sheet_name="Logs")
print(consecutive_numbers1(logs))