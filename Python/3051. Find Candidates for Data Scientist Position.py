# Table: Candidates
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | candidate_id | int     |
# | skill        | varchar |
# +--------------+---------+
# (candidate_id, skill) is the primary key (columns with unique values) for this table.
# Each row includes candidate_id and skill.
# Write a query to find the candidates best suited for a Data Scientist position.
# The candidate must be proficient in Python, Tableau, and PostgreSQL.
#
# Return the result table ordered by candidate_id in ascending order.
import pandas as pd

def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    grouped = (candidates
                .groupby(by="candidate_id", as_index=False)
                .agg(skill=("skill", lambda x: set(x))))
    return grouped.loc[grouped["skill"] >= {"Python", "PostgreSQL", "Tableau"}, ["candidate_id"]].sort_values(by="candidate_id", ascending=True)
