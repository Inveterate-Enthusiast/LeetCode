# Table: Candidate
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | name        | varchar  |
# +-------------+----------+
# id is the column with unique values for this table.
# Each row of this table contains information about the id and the name of a candidate.
#
#
# Table: Vote
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | candidateId | int  |
# +-------------+------+
# id is an auto-increment primary key (column with unique values).
# candidateId is a foreign key (reference column) to id from the Candidate table.
# Each row of this table determines the candidate who got the ith vote in the elections.
#
#
# Write a solution to report the name of the winning candidate (i.e., the candidate who got the largest number of votes).
#
# The test cases are generated so that exactly one candidate wins the elections.
import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(
        left=(
            vote.groupby(by="candidateId", as_index=False)
            .agg(count=("id", "nunique"))
        ),
        right=candidate,
        how="left",
        left_on="candidateId",
        right_on="id",
    ).query("count == count.max()").loc[:, ["name"]]