# Table:  logs
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | log_id      | int     |
# | ip          | varchar |
# | status_code | int     |
# +-------------+---------+
# log_id is the unique key for this table.
# Each row contains server access log information including IP address and HTTP status code.
# Write a solution to find invalid IP addresses. An IPv4 address is invalid if it meets any of these conditions:
#
# Contains numbers greater than 255 in any octet
# Has leading zeros in any octet (like 01.02.03.04)
# Has less or more than 4 octets
# Return the result table ordered by invalid_count, ip in descending order respectively.

import pandas as pd
import numpy as np
from pathlib import Path
import os

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    logs["list"] = logs["ip"].str.split(".")
    logs["int"] = logs["list"].apply(lambda x: list(map(int, x)))
    logs[["min", "max"]] = logs["int"].apply(lambda x: pd.Series([min(x), max(x)]))
    logs["len"] = logs["list"].apply(len)
    logs["first"] = logs["list"].apply(lambda x: min(map(int, [i[0] for i in x])))
    logs["bool"] = np.where(
        logs["first"] == 0, 1,
        np.where(
            logs["len"] != 4, 1,
            np.where(
                logs["max"] > 255, 1, 0
            )
        )
    )
    result = logs.groupby(by="ip", as_index=False).agg(filter=("bool", "sum"), invalid_count=("ip", "count")).query("filter > 0")
    return result.drop(labels=["filter"], axis=1).sort_values(by=["invalid_count", "ip"], ascending=[False, False])

logs = pd.read_excel(Path(os.getcwd()) / "data" / "3451. Find Invalid IP Addresses.xlsx")
print(find_invalid_ips(logs))