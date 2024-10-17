# Table: Users
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | user_id     | int      |
# | item        | varchar  |
# | created_at  | datetime |
# | amount      | int      |
# +-------------+----------+
# This table may contain duplicate records.
# Each row includes the user ID, the purchased item, the date of purchase, and the purchase amount.
# Write a solution to identify active users. An active user is a user that has made a second purchase within 7 days of
# any other of their purchases.
#
# For example, if the ending date is May 31, 2023. So any date between May 31, 2023, and June 7, 2023 (inclusive)
# would be considered "within 7 days" of May 31, 2023.
#
# Return a list of user_id which denotes the list of active users in any order.
import pandas as pd

def find_active_users(users: pd.DataFrame) -> pd.DataFrame:
    users.sort_values(by=["user_id", "created_at"], ascending=[True, True], inplace=True)
    users["prev_date"] = users.groupby(by="user_id", as_index=False)["created_at"].shift(1)
    users["dif"] = (users["created_at"] - users["prev_date"]).dt.days
    return users.loc[users["dif"] <= 7, ["user_id"]].drop_duplicates()