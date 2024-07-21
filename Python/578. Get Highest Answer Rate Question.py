# Table: SurveyLog
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | action      | ENUM |
# | question_id | int  |
# | answer_id   | int  |
# | q_num       | int  |
# | timestamp   | int  |
# +-------------+------+
# This table may contain duplicate rows.
# action is an ENUM (category) of the type: "show", "answer", or "skip".
# Each row of this table indicates the user with ID = id has taken an action with the question question_id at time timestamp.
# If the action taken by the user is "answer", answer_id will contain the id of that answer, otherwise, it will be null.
# q_num is the numeral order of the question in the current session.
#
#
# The answer rate for a question is the number of times a user answered the question by the number of times a user showed the question.
#
# Write a solution to report the question that has the highest answer rate. If multiple questions have the same maximum answer rate, report the question with the smallest question_id.
import pandas as pd
from pathlib import Path
import os


def grouping(df: pd.DataFrame) -> float:
    return ((df.loc[df["action"] == "answer"]["action"].count()) / (df.loc[df["action"] == "show"]["action"].count()))

def get_the_question(survey_log: pd.DataFrame) -> pd.DataFrame:
    if survey_log.empty:
        return pd.DataFrame(columns=["survey_log"])

    return (survey_log
            .groupby(by=["id", "question_id"], as_index=True)
            .apply(grouping, include_groups=False)
            .reset_index()
            .rename(columns={"question_id": "survey_log", 0: "rate"})
            .sort_values(by=["rate", "survey_log"], ascending=[False, True])
            .iloc[0:1][["survey_log"]])

path = Path(os.getcwd()) / "data" / "578. Get Highest Answer Rate Question.xlsx"
survey_log = pd.read_excel(path)
print(get_the_question(survey_log))