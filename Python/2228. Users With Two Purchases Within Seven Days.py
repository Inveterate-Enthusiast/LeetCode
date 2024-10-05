# Table: Purchases
#
# +---------------+------+
# | Column Name   | Type |
# +---------------+------+
# | purchase_id   | int  |
# | user_id       | int  |
# | purchase_date | date |
# +---------------+------+
# purchase_id contains unique values.
# This table contains logs of the dates that users purchased from a certain retailer.
#
#
# Write a solution to report the IDs of the users that made any two purchases at most 7 days apart.
#
# Return the result table ordered by user_id.
import pandas as pd

def find_valid_users(purchases: pd.DataFrame) -> pd.DataFrame:
    purchases.sort_values(by=["user_id", "purchase_date"], ascending=[True, True], inplace=True)
    purchases["diff"] = purchases.groupby(by="user_id", as_index=False)["purchase_date"].transform(lambda x: (x - x.shift()).dt.days)
    return purchases.loc[purchases["diff"] <= 7, ["user_id"]].drop_duplicates().sort_values(by="user_id", ascending=True)

