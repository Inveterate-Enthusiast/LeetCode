# Table: Scores
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student_id  | int     |
# | subject     | varchar |
# | score       | int     |
# | exam_date   | varchar |
# +-------------+---------+
# (student_id, subject, exam_date) is the primary key for this table.
# Each row contains information about a student's score in a specific subject on a particular exam date. score is between 0 and 100 (inclusive).
# Write a solution to find the students who have shown improvement. A student is considered to have shown
# improvement if they meet both of these conditions:
#
# Have taken exams in the same subject on at least two different dates
# Their latest score in that subject is higher than their first score
# Return the result table ordered by student_id, subject in ascending order.
import pandas as pd
import numpy as np

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    sub_prev = pd.merge(
        left=scores.groupby(by=["student_id", "subject"]).agg(exam_date=("exam_date", "min")),
        right=scores,
        how="inner",
        on=["student_id", "subject", "exam_date"]
    )

    sub_cur = pd.merge(
        left=scores.groupby(by=["student_id", "subject"]).agg(exam_date=("exam_date", "max")),
        right=scores,
        how="inner",
        on=["student_id", "subject", "exam_date"]
    )

    crossed = pd.merge(
        left=sub_prev,
        right=sub_cur,
        how="inner",
        on=["student_id", "subject"],
        suffixes=("_prev", "_cur")
    ).query("exam_date_prev < exam_date_cur")

    crossed["flag"] = np.where(crossed["score_prev"] < crossed["score_cur"], 0, 1)
    return (crossed.loc[crossed["flag"] == 0, ["student_id", "subject", "score_prev", "score_cur"]]
            .rename(columns={"score_prev": "first_score", "score_cur": "latest_score"})
            .sort_values(by=["student_id", "subject"], ascending=[True, True]))

def find_students_who_improved1(scores: pd.DataFrame) -> pd.DataFrame:
    grouped = scores.groupby(by=["student_id", "subject"], as_index=False).agg(date_prev=("exam_date", "min"), date_cur=("exam_date", "max"))
    merged = pd.merge(
        left=grouped.rename(columns={"date_prev": "exam_date"}),
        right=scores.rename(columns={"score": "first_score"}),
        how="inner",
        on=["student_id", "subject", "exam_date"]
    ).rename(columns={"exam_date": "date_prev"})
    merged = pd.merge(
        left=merged.rename(columns={"date_cur": "exam_date"}),
        right=scores.rename(columns={"score": "latest_score"}),
        how="inner",
        on=["student_id", "subject", "exam_date"]
    ).rename(columns={"exam_date": "date_cur"})
    return merged.loc[
        (merged["date_prev"] < merged["date_cur"])
        &
        (merged["first_score"] < merged["latest_score"]),
        ["student_id", "subject", "first_score", "latest_score"]
    ].sort_values(by=["student_id", "subject"], ascending=[True, True])