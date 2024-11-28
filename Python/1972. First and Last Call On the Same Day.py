# Table: Calls
#
# +--------------+----------+
# | Column Name  | Type     |
# +--------------+----------+
# | caller_id    | int      |
# | recipient_id | int      |
# | call_time    | datetime |
# +--------------+----------+
# (caller_id, recipient_id, call_time) is the primary key (combination of columns with unique values) for this table.
# Each row contains information about the time of a phone call between caller_id and recipient_id.
#
#
# Write a solution to report the IDs of the users whose first and last calls on any day were with the same person.
# Calls are counted regardless of being the caller or the recipient.
#
# Return the result table in any order.

import pandas as pd

def same_day_calls(calls: pd.DataFrame) -> pd.DataFrame:
    concated = pd.concat([
        calls,
        calls.rename(columns={"caller_id" : "recipient_id", "recipient_id": "caller_id"})[["caller_id", "recipient_id", "call_time"]]
    ])
    concated["date"] = concated["call_time"].dt.date
    concated["first_call"] = concated.groupby(by=["caller_id", "date"], as_index=False)["call_time"].rank(method="dense", ascending=True)
    concated["last_call"] = concated.groupby(by=["caller_id", "date"], as_index=False)["call_time"].rank(method="dense", ascending=False)
    merged = pd.merge(
        left=concated,
        right=concated,
        how="inner",
        left_on=["caller_id", "recipient_id", "first_call"],
        right_on=["caller_id", "recipient_id", "last_call"],
        suffixes=("_first", "_last")
    ).query("(first_call_first == 1) & (last_call_last == 1)")
    return merged[["caller_id"]].rename(columns={"caller_id": "user_id"}).drop_duplicates(keep="first")