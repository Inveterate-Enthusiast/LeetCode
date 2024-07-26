# Table: Spending
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | user_id     | int     |
# | spend_date  | date    |
# | platform    | enum    |
# | amount      | int     |
# +-------------+---------+
# The table logs the history of the spending of users that make purchases from an online shopping website that has a desktop and a mobile application.
# (user_id, spend_date, platform) is the primary key (combination of columns with unique values) of this table.
# The platform column is an ENUM (category) type of ('desktop', 'mobile').
#
#
# Write a solution to find the total number of users and the total amount spent using the mobile only, the desktop only, and both mobile and desktop together for each date.
#
# Return the result table in any order.
import pandas as pd
import os
from pathlib import Path

def user_purchase(spending: pd.DataFrame) -> pd.DataFrame:
    unique_date = pd.DataFrame({
        "spend_date": spending["spend_date"].unique()
    }).merge(
        right=pd.DataFrame({
            "platform": list(y := spending["platform"].unique()) + ["both"]
        }),
        how="cross"
    )


    spending["platform"] = spending.groupby(by=["spend_date", "user_id"], as_index=False)["platform"].transform(lambda x: "both" if set(x) == set(y) else x)
    grouped = spending.groupby(by=["spend_date", "platform"], as_index=False, dropna=False).agg(total_amount=("amount", "sum"), total_users=("user_id", "nunique"))
    return pd.merge(
        left=unique_date,
        right=grouped,
        how="left",
        on=["spend_date", "platform"]
    ).fillna(0)

path = Path(os.getcwd()) / "data" / "1127. User Purchase Platform.xlsx"
spending = pd.read_excel(path)
print(user_purchase(spending))