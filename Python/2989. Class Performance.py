# Table: Scores
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | student_id   | int     |
# | student_name | varchar |
# | assignment1  | int     |
# | assignment2  | int     |
# | assignment3  | int     |
# +--------------+---------+
# student_id is column of unique values for this table.
# This table contains student_id, student_name, assignment1, assignment2, and assignment3.
# Write a solution to calculate the difference in the total score (sum of all 3 assignments)
# between the highest score obtained by students and the lowest score obtained by them.
#
# Return the result table in any order.
import pandas as pd

def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
    scores["total"] = scores["assignment1"] + scores["assignment2"] + scores["assignment3"]
    return pd.DataFrame({
        "difference_in_score": [(scores["total"].max() - scores["total"].min())]
    })
