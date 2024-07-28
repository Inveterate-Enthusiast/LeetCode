# Table: Playback
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | session_id  | int  |
# | customer_id | int  |
# | start_time  | int  |
# | end_time    | int  |
# +-------------+------+
# session_id is the column with unique values for this table.
# customer_id is the ID of the customer watching this session.
# The session runs during the inclusive interval between start_time and end_time.
# It is guaranteed that start_time <= end_time and that two sessions for the same customer do not intersect.
#
#
# Table: Ads
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | ad_id       | int  |
# | customer_id | int  |
# | timestamp   | int  |
# +-------------+------+
# ad_id is the column with unique values for this table.
# customer_id is the ID of the customer viewing this ad.
# timestamp is the moment of time at which the ad was shown.
#
#
# Write a solution to report all the sessions that did not get shown any ads.
#
# Return the result table in any order.
import pandas as pd

def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=playback,
        right=ads,
        how="outer",
        on="customer_id"
    )
    merged["bool"] = merged.apply(lambda x: False if x["timestamp"] is pd.NA or not (x["start_time"] <= x["timestamp"] <= x["end_time"]) else True, axis=1)
    return merged.groupby(by="session_id", as_index=False).agg(answer=("bool", "sum")).query("answer == 0")[["session_id"]]