# Table: Sessions
#
# +---------------------+---------+
# | Column Name         | Type    |
# +---------------------+---------+
# | session_id          | int     |
# | duration            | int     |
# +---------------------+---------+
# session_id is the column of unique values for this table.
# duration is the time in seconds that a user has visited the application.
#
# You want to know how long a user visits your application.
# You decided to create bins of "[0-5>", "[5-10>", "[10-15>", and "15 minutes or more" and count the number of sessions on it.
#
# Write a solution to report the (bin, total).
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os
from collections import defaultdict

def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:
    ans = defaultdict(int)
    ans["[0-5>"] = sum(sessions["duration"].between(0*60, 5*60, inclusive="left"))
    ans["[5-10>"] = sum(sessions["duration"].between(5*60, 10*60, inclusive="left"))
    ans["[10-15>"] = sum(sessions["duration"].between(10*60, 15*60, inclusive="left"))
    ans["15 or more"] = sum(sessions["duration"].between(15*60, float("inf"), inclusive="left"))

    return pd.DataFrame(ans.items(), columns=["bin", "total"])

def create_bar_chart1(sessions: pd.DataFrame) -> pd.DataFrame:
    return pd.cut(
        x=sessions["duration"],
        labels=["[0-5>", "[5-10>", "[10-15>", "15 or more"],
        bins=[0, 5*60, 10*60, 15*60, float("inf")],
        include_lowest=True,
        right=False,
        retbins=False
    ).value_counts().reset_index(name="total").rename(columns={"duration": "bin"})


path = Path(os.getcwd()) / "data" / "1435. Create a Session Bar Chart.xlsx"
sessions = pd.read_excel(path)
print(create_bar_chart1(sessions))


