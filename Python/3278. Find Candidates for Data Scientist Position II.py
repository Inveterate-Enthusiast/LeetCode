# Table: Candidates
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | candidate_id | int     |
# | skill        | varchar |
# | proficiency  | int     |
# +--------------+---------+
# (candidate_id, skill) is the unique key for this table.
# Each row includes candidate_id, skill, and proficiency level (1-5).
# Table: Projects
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | project_id   | int     |
# | skill        | varchar |
# | importance   | int     |
# +--------------+---------+
# (project_id, skill) is the primary key for this table.
# Each row includes project_id, required skill, and its importance (1-5) for the project.
# Leetcode is staffing for multiple data science projects. Write a solution to find the best candidate for each project based on the following criteria:
#
# Candidates must have all the skills required for a project.
# Calculate a score for each candidate-project pair as follows:
# Start with 100 points
# Add 10 points for each skill where proficiency > importance
# Subtract 5 points for each skill where proficiency < importance
# Include only the top candidate (highest score) for each project. If there’s a tie, choose the candidate with the lower candidate_id.
# If there is no suitable candidate for a project, do not return that project.
#
# Return a result table ordered by project_id in ascending order.

import pandas as pd
import numpy as np
from pathlib import Path
import os


def find_best_candidates(candidates: pd.DataFrame, projects: pd.DataFrame) -> pd.DataFrame:
    candidates["can_set"] = candidates["candidate_id"].map(candidates.groupby(by="candidate_id")["skill"].apply(set))
    projects["pro_set"] = projects["project_id"].map(projects.groupby(by="project_id")["skill"].apply(set))
    merged = pd.merge(
        left=projects,
        right=candidates,
        how="left",
        on="skill"
    )
    filtered = merged.loc[merged["pro_set"] <= merged["can_set"]].copy()
    filtered["score"] = np.where(
        filtered["proficiency"] > filtered["importance"], 10,
        np.where(
            filtered["proficiency"] < filtered["importance"], (-5),
            0
        )
    )
    grouped = filtered.groupby(by=["project_id", "candidate_id"], as_index=False).agg(score=("score", lambda x: 100 + x.sum()))
    grouped.sort_values(by=["project_id", "score", "candidate_id"], ascending=[True, False, True], inplace=True)
    grouped["rank"] = grouped.groupby(by="project_id", as_index=False).cumcount() + 1
    return grouped.loc[grouped["rank"] == 1, ["project_id", "candidate_id", "score"]]

path = Path(os.getcwd()) / "data" / "3278. Find Candidates for Data Scientist Position II.xlsx"
candidates = pd.read_excel(path, sheet_name="Candidates")
projects = pd.read_excel(path, sheet_name="Projects")
print(find_best_candidates(candidates, projects).to_string())