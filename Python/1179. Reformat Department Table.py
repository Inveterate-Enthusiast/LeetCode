# Table: Department
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | revenue     | int     |
# | month       | varchar |
# +-------------+---------+
# In SQL,(id, month) is the primary key of this table.
# The table has information about the revenue of each department per month.
# The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].

# Reformat the table such that there is a department id column and a revenue column for each month.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os
from datetime import datetime
from collections import defaultdict



def reformat_table(department: pd.DataFrame) -> pd.DataFrame: # правильный, но не нравится LeetCode
    _dict = defaultdict(defaultdict)

    for id in department["id"].unique():
        for month in department[department["id"] == id]["month"].unique():
            _dict[str(id)][str(month)] = department[
                (department["id"] == id) &
                (department["month"] == month)
            ].iloc[0]["revenue"]

    ansDF = pd.DataFrame({"id": [i for i in _dict.keys()]})
    for id in _dict.keys():
        index = ansDF[ansDF["id"] == id].index
        for i in range(1, 12+1):
            month = datetime(1900, i, 1).strftime("%b")
            column_name = month + "_Revenue"
            if column_name not in ansDF:
                ansDF[column_name] = pd.Series()
            ansDF.loc[index, column_name] = _dict[id].get(month, None)

    return ansDF

def reformat_table1(department: pd.DataFrame) -> pd.DataFrame:
    our_pivot = department.pivot_table(
        index="id",
        columns="month",
        values="revenue",
        aggfunc="sum",
        fill_value=pd.NA
    ).reset_index().sort_values(by="id", ascending=True)

    ansDF = pd.DataFrame({"id": pd.Series(our_pivot["id"].unique())})
    for i in range(1, 12+1):
        month = datetime(1900, i, 1).strftime("%b")
        column_name = month + "_Revenue"
        ansDF[column_name] = None
        if month in our_pivot:
            ansDF[column_name] = our_pivot[month]
    return ansDF

def reformat_table2(department: pd.DataFrame) -> pd.DataFrame:
    our_pivot = department.pivot_table(index="id", columns="month", values="revenue", aggfunc="sum", fill_value=pd.NA).reset_index().sort_values(by="id", ascending=True)
    ansDF = pd.DataFrame(columns=["id"] + [datetime(1900, i, 1).strftime("%b") for i in range(1, 12+1)])

    for column in ansDF.columns:
        if column in our_pivot:
            ansDF[column] = our_pivot[column]
        if column != "id":
            ansDF.rename(columns={column: column + "_Revenue"}, inplace=True)

    return ansDF




path = Path(os.getcwd()) / "data" / "1179. Reformat Department Table.xlsx"
department = pd.read_excel(path)
print(reformat_table2(department))
# print(department[["month", "revenue"]].to_dict())
