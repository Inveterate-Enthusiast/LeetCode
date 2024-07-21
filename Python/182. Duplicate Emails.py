# Table: Person
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | email       | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains an email. The emails will not contain uppercase letters.

# Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
#
# Return the result table in any order.
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    second_person = person.copy().drop_duplicates(subset="email", keep="last", inplace=False)
    person.drop_duplicates(subset="email", keep="first", inplace=True)
    ans_df = pd.merge(
        left = person,
        right = second_person,
        on = "email",
        how = "inner",
        suffixes = ("_f", "_s")
    )
    return ans_df[ans_df["id_f"] != ans_df["id_s"]][["email"]].rename(columns={"email": "Email"})

def duplicate_emails1(person: pd.DataFrame) -> pd.DataFrame:
    ans_df: pd.DataFrame = person.loc[person.duplicated(subset="email", keep="first"), ["email"]]
    return ans_df.drop_duplicates(subset="email").rename(columns={"email": "Email"})

def duplicate_emails2(person: pd.DataFrame) -> pd.DataFrame:
    return person.loc[
        person.duplicated(subset="email", keep="first"),
        ["email"]
    ].drop_duplicates()

Person = pd.DataFrame({
    "id": [1, 2, 3],
    "email": ["a@b.com", "c@d.com", "a@b.com"]
})

print(duplicate_emails2(Person))