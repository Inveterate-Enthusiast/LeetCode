# Table: Servers
#
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | server_id      | int      |
# | status_time    | datetime |
# | session_status | enum     |
# +----------------+----------+
# (server_id, status_time, session_status) is the primary key (combination of columns with unique values) for this table.
# session_status is an ENUM (category) type of ('start', 'stop').
# Each row of this table contains server_id, status_time, and session_status.
# Write a solution to find the total time when servers were running. The output should be rounded down to the nearest number of full days.
#
# Return the result table in any order.


import pandas as pd
import numpy as np

def server_utilization_time(servers: pd.DataFrame) -> pd.DataFrame:
    servers["row"] = np.arange(1, len(servers) + 1)
    servers["dif"] = np.where(
        (servers["row"] % 2) == 0,
        (servers["status_time"] - servers["status_time"].shift(1)).dt.total_seconds(),
        0
    )
    return pd.DataFrame({
        "total_uptime_days": [np.floor(servers["dif"].sum() / 60 / 60 / 24)]
    })
