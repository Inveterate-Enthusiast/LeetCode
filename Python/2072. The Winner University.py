# Table: NewYork
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | student_id  | int  |
# | score       | int  |
# +-------------+------+
# In SQL, student_id is the primary key for this table.
# Each row contains information about the score of one student from New York University in an exam.
#
#
# Table: California
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | student_id  | int  |
# | score       | int  |
# +-------------+------+
# In SQL, student_id is the primary key for this table.
# Each row contains information about the score of one student from California University in an exam.
#
#
# There is a competition between New York University and California University.
# The competition is held between the same number of students from both universities.
# The university that has more excellent students wins the competition.
# If the two universities have the same number of excellent students, the competition ends in a draw.
#
# An excellent student is a student that scored 90% or more in the exam.
#
# Return:
#
# "New York University" if New York University wins the competition.
# "California University" if California University wins the competition.
# "No Winner" if the competition ends in a draw.
import pandas as pd

def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    n = new_york.loc[new_york["score"] >= 90].shape[0]
    c = california.loc[california["score"] >= 90].shape[0]
    return pd.DataFrame({
        "winner": [("New York University" if n > c else ("California University" if c > n else "No Winner"))]
    })
