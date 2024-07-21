# Table: Signups
#
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | user_id        | int      |
# | time_stamp     | datetime |
# +----------------+----------+
# user_id is the column of unique values for this table.
# Each row contains information about the signup time for the user with ID user_id.
#
#
# Table: Confirmations
#
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | user_id        | int      |
# | time_stamp     | datetime |
# | action         | ENUM     |
# +----------------+----------+
# (user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
# user_id is a foreign key (reference column) to the Signups table.
# action is an ENUM (category) of the type ('confirmed', 'timeout')
# Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').
#
#
# The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.
#
# Write a solution to find the confirmation rate of each user.
#
# Return the result table in any order.
import pandas as pd


def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    grouped = (confirmations
               .groupby(by="user_id", as_index=False, dropna=False)
               .agg(confirmation_rate=("action",
                                       lambda x: round(((x[x == "confirmed"].count() / i) if (i := x.count()) else 0), 2))))
    return pd.merge(
        left=grouped,
        right=signups,
        on="user_id",
        how="right"
    ).fillna(0, downcast="infer").loc[:, ["user_id", "confirmation_rate"]]