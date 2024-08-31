# Table: Accounts
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+
# id is the primary key (column with unique values) for this table.
# This table contains the account id and the user name of each account.
#
#
# Table: Logins
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | login_date    | date    |
# +---------------+---------+
# This table may contain duplicate rows.
# This table contains the account id of the user who logged in and the login date. A user may log in multiple times in the day.
#
#
# Active users are those who logged in to their accounts for five or more consecutive days.
#
# Write a solution to find the id and the name of active users.
#
# Return the result table ordered by id.
import pandas as pd
from pathlib import Path
import os

def active_users(accounts: pd.DataFrame, logins: pd.DataFrame) -> pd.DataFrame:
    logins.drop_duplicates(subset=["id", "login_date"], keep="first", inplace=True)
    logins["days"] = logins.groupby(by="id", as_index=False)["login_date"].transform(lambda x: (x - x.min() + pd.Timedelta(value=1, unit="d")).dt.days)
    logins["rank"] = logins.groupby(by="id", as_index=False)["login_date"].rank(method="dense", ascending=True)
    logins["diff"] = logins["days"] - logins["rank"]
    return pd.merge(
        left=(logins
              .groupby(by=["id", "diff"], as_index=False)
              .agg(count=("diff", "count"))
              .query("count >= 5")
              .drop_duplicates(subset="id", keep="first")),
        right=accounts,
        on="id",
        how="left"
    )[["id", "name"]].sort_values(by="id", ascending=True)


path = Path(os.getcwd()) / "data" / "1454. Active Users.xlsx"
accounts = pd.read_excel(path, sheet_name="Accounts")
logins = pd.read_excel(path, sheet_name="Logins")
print(active_users(accounts, logins))