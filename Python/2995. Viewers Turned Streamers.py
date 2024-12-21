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
# Write a solution to find the number of streaming sessions for users whose first session was as a viewer.
#
# Return the result table ordered by count of streaming sessions, user_id in descending order.


import pandas as pd

def count_turned_streamers(sessions: pd.DataFrame) -> pd.DataFrame:
    sessions.sort_values(by=["user_id", "session_start", "session_end"], ascending=[True, True, True], inplace=True)
    sessions["rank"] = sessions.groupby(by="user_id", as_index=False)["session_id"].cumcount() + 1
    merged = pd.merge(
        left=sessions,
        right=sessions.loc[sessions["rank"] == 1, ["user_id", "session_type"]].rename(columns={"session_type": "first_type"}),
        how="left",
        on="user_id"
    )
    grouped = merged.loc[
        (merged["first_type"] == "Viewer")
        &
        (merged["session_type"] == "Streamer")
    ].groupby(by="user_id", as_index=False).agg(sessions_count=("session_id", "nunique"))
    return grouped.sort_values(by=["sessions_count", "user_id"], ascending=[False, False])