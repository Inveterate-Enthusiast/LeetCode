# Table: Sessions
#
# +---------------+----------+
# | Column Name   | Type     |
# +---------------+----------+
# | user_id       | int      |
# | session_start | datetime |
# | session_end   | datetime |
# | session_id    | int      |
# | session_type  | enum     |
# +---------------+----------+
# session_id is column of unique values for this table.
# session_type is an ENUM (category) type of (Viewer, Streamer).
# This table contains user id, session start, session end, session id and session type.
# Write a solution to find the the users who have had at least one consecutive session of the same type
# (either 'Viewer' or 'Streamer') with a maximum gap of 12 hours between sessions.
#
# Return the result table ordered by user_id in ascending order.



import pandas as pd
import numpy as np

def user_activities(sessions: pd.DataFrame) -> pd.DataFrame:
    sessions.sort_values(by=["user_id", "session_start", "session_end"], ascending=[True, True, True], inplace=True)
    sessions["prev_end"] = sessions.groupby(by=["user_id", "session_type"], as_index=False)["session_end"].shift(1)
    sessions["bool"] = np.where(
        (~sessions["prev_end"].isna())
        &
        (((sessions["session_start"] - sessions["prev_end"]).dt.total_seconds() / (60 * 60)) <= 12),
        1, 0
    )
    return (sessions
            .groupby(by=["user_id", "session_type"], as_index=False)
            .agg(days=("bool", "sum"))
            .query("days >= 1")
            [["user_id"]].drop_duplicates(keep="first"))