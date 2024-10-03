# Table: Genders
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | user_id     | int     |
# | gender      | varchar |
# +-------------+---------+
# user_id is the primary key (column with unique values) for this table.
# gender is ENUM (category) of type 'female', 'male', or 'other'.
# Each row in this table contains the ID of a user and their gender.
# The table has an equal number of 'female', 'male', and 'other'.
#
#
# Write a solution to rearrange the Genders table such that the rows alternate between 'female', 'other', and 'male' in order.
# The table should be rearranged such that the IDs of each gender are sorted in ascending order.
#
# Return the result table in the mentioned order.
import pandas as pd
import numpy as np

def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
    genders["our_rank"] = genders.groupby(by="gender", as_index=False)["user_id"].rank(method="dense", ascending=True)
    genders["pos"] = np.where(genders["gender"] == "female", 1, (np.where(genders["gender"] == "other", 2, 3)))
    genders.sort_values(by=["our_rank", "pos"], ascending=[True, True], inplace=True)
    return genders[["user_id", "gender"]]
