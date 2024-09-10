# Table: emails
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | email_id    | int      |
# | user_id     | int      |
# | signup_date | datetime |
# +-------------+----------+
# (email_id, user_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the email ID, user ID, and signup date.
# Table: texts
#
# +---------------+----------+
# | Column Name   | Type     |
# +---------------+----------+
# | text_id       | int      |
# | email_id      | int      |
# | signup_action | enum     |
# | action_date   | datetime |
# +---------------+----------+
# (text_id, email_id) is the primary key (combination of columns with unique values) for this table.
# signup_action is an enum type of ('Verified', 'Not Verified').
# Each row of this table contains the text ID, email ID, signup action, and action date.
# Write a Solution to find the user IDs of those who verified their sign-up on the second day.
#
# Return the result table ordered by user_id in ascending order.
import pandas as pd

def find_second_day_signups(emails: pd.DataFrame, texts: pd.DataFrame) -> pd.DataFrame:
    emails["action_date"] = (pd.to_datetime(emails["signup_date"]) + pd.Timedelta(value=1, unit="d")).dt.normalize()
    texts["action_date"] = texts["action_date"].dt.normalize()
    merged = pd.merge(
        left=emails,
        right=texts,
        how="inner",
        on=["email_id", "action_date"]
    )
    return (merged
            .loc[merged["signup_action"] == "Verified", ["user_id"]]
            .drop_duplicates(subset="user_id", keep="first")
            .sort_values(by="user_id", ascending=True))