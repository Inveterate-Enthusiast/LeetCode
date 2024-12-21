# Table: Votes
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | voter       | varchar |
# | candidate   | varchar |
# +-------------+---------+
# (voter, candidate) is the primary key (combination of unique values) for this table.
# Each row of this table contains name of the voter and their candidate.
# The election is conducted in a city where everyone can vote for one or more candidates or choose not to vote.
# Each person has 1 vote so if they vote for multiple candidates, their vote gets equally split across them.
# For example, if a person votes for 2 candidates, these candidates receive an equivalent of 0.5 votes each.
#
# Write a solution to find candidate who got the most votes and won the election.
# Output the name of the candidate or If multiple candidates have an equal number of votes,
# display the names of all of them.
#
# Return the result table ordered by candidate in ascending order.


import pandas as pd

def get_election_results(votes: pd.DataFrame) -> pd.DataFrame:
    votes["num"] = votes.groupby(by="voter", as_index=False)["candidate"].transform("nunique")
    votes["score"] = 1 / votes["num"]
    grouped = votes.groupby(by="candidate", as_index=False).agg(score=("score", "sum"))
    return grouped.loc[grouped["score"] == grouped["score"].max(), ["candidate"]].sort_values(by="candidate", ascending=True)