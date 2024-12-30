# Table: SecretSanta
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | giver_id    | int  |
# | receiver_id | int  |
# | gift_value  | int  |
# +-------------+------+
# (giver_id, receiver_id) is the unique key for this table.
# Each row represents a record of a gift exchange between two employees, giver_id represents the employee who gives a gift,
# receiver_id represents the employee who receives the gift and gift_value represents the value of the gift given.
# Write a solution to find the total gift value and length of circular chains of Secret Santa gift exchanges:
#
# A circular chain is defined as a series of exchanges where:
#
# Each employee gives a gift to exactly one other employee.
# Each employee receives a gift from exactly one other employee.
# The exchanges form a continuous loop (e.g., employee A gives a gift to B, B gives to C, and C gives back to A).
# Return the result ordered by the chain length and total gift value of the chain in descending order.

import pandas as pd
from collections import deque
from pathlib import Path
import os

def find_gift_chains(secret_santa: pd.DataFrame) -> pd.DataFrame:
    result = list()
    while not secret_santa.empty:
        cur_value = 0
        cur_len = 0
        queue = deque()
        queue.append(secret_santa.index[0])
        while queue:
            index = queue.popleft()
            receiver = secret_santa.loc[index, "receiver_id"]
            cur_len += 1
            cur_value += secret_santa.loc[index, "gift_value"]
            new_giver = secret_santa.loc[secret_santa["giver_id"] == receiver]
            if not new_giver.empty:
                new_index = new_giver.index[0]
                queue.append(new_index)
            secret_santa = secret_santa.drop(index)
        result.append([cur_len, cur_value])
    return (pd
            .DataFrame(data=result, columns=["chain_length", "total_gift_value"])
            .sort_values(by=["chain_length", "total_gift_value"], ascending=[False, False])
            .drop_duplicates()
            .reset_index(drop=True)
            .assign(chain_id = lambda x: x.index + 1)
            [["chain_id", "chain_length", "total_gift_value"]])




secret_santa = pd.read_excel(Path(os.getcwd()) / "data" / "3401. Find Circular Gift Exchange Chains.xlsx")
print(find_gift_chains(secret_santa))