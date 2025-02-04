# Table: Users
#
# +-----------------+---------+
# | Column Name     | Type    |
# +-----------------+---------+
# | user_id         | int     |
# | email           | varchar |
# +-----------------+---------+
# (user_id) is the unique key for this table.
# Each row contains a user's unique ID and email address.
# Write a solution to find all the valid email addresses. A valid email address meets the following criteria:
#
# It contains exactly one @ symbol.
# It ends with .com.
# The part before the @ symbol contains only alphanumeric characters and underscores.
# The part after the @ symbol and before .com contains a domain name that contains only letters.
# Return the result table ordered by user_id in ascending order.


import pandas as pd
import re

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r"\w+\@[^\W\d_]+\.com"
    users["bool"] = users["email"].apply(lambda x: True if re.findall(pattern, x) else False)
    return users.loc[users["bool"]].drop(labels="bool", axis=1).sort_values(by="user_id", ascending=True)