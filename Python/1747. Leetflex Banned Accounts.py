# Table: LogInfo
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | account_id  | int      |
# | ip_address  | int      |
# | login       | datetime |
# | logout      | datetime |
# +-------------+----------+
# This table may contain duplicate rows.
# The table contains information about the login and logout dates of Leetflex accounts.
# It also contains the IP address from which the account was logged in and out.
# It is guaranteed that the logout time is after the login time.
#
#
# Write a solution to find the account_id of the accounts that should be banned from Leetflex.
# An account should be banned if it was logged in at some moment from two different IP addresses.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os

def grouping(df: pd.DataFrame) -> pd.Series:
    past_logout = None
    past_ip = None
    for index, row in df.sort_values(by="login", ascending=True).iterrows():
        if not past_logout:
            pass
        elif row["login"] <= past_logout and row["ip_address"] != past_ip:
            return pd.Series(data=True, index=["our_bool"])

        if not past_logout or past_logout <= row["logout"]:
            past_logout = row["logout"]
            past_ip = row["ip_address"]
    return pd.Series(data=False, index=["our_bool"])


def leetflex_banned_accnts(log_info: pd.DataFrame) -> pd.DataFrame:
    if log_info.empty:
        return log_info[["account_id"]]
    grouped = log_info.groupby(by="account_id", as_index=False).apply(grouping, include_groups=False)
    return grouped.loc[grouped["our_bool"], ["account_id"]]

def leetflex_banned_accnts1(log_info: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=log_info,
        right=log_info,
        how="inner",
        on="account_id",
        suffixes=("_left", "_right")
    )
    return merged.loc[
        (merged["login_left"].between(merged["login_right"], merged["logout_right"], inclusive="both"))
        &
        (merged["ip_address_left"] != merged["ip_address_right"]),
        ["account_id"]
    ].drop_duplicates()

log_info = pd.read_excel(Path(os.getcwd()) / "data" / "1747. Leetflex Banned Accounts.xlsx")
print(leetflex_banned_accnts(log_info))