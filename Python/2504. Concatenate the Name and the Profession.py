# Table: Person
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | person_id   | int     |
# | name        | varchar |
# | profession  | ENUM    |
# +-------------+---------+
# person_id is the primary key (column with a unique value) for this table.
# Each row in this table contains a person's ID, name, and profession.
# The profession column in an enum of the type ('Doctor', 'Singer', 'Actor', 'Player', 'Engineer', or 'Lawyer')
#
#
# Write a solution to report each person's name followed by the first letter of their profession enclosed in parentheses.
#
# Return the result table ordered by person_id in descending order.


import pandas as pd

def concatenate_info(person: pd.DataFrame) -> pd.DataFrame:
    person["name"] = person.apply(lambda x: x["name"] + "(" + x["profession"][0] + ")", axis=1)
    return person[["person_id", "name"]].sort_values(by="person_id", ascending=False)