# Table: Emails
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | email       | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains an email. The emails will not contain uppercase letters.
# Write a solution to find all unique email domains and count the number of individuals associated with each domain. Consider only those domains that end with .com.
#
# Return the result table orderd by email domains in ascending order.
import pandas as pd
import re
from pathlib import Path
import os

def find_unique_email_domains(emails: pd.DataFrame) -> pd.DataFrame:
    pattern = r".*?@(.*\.com)"
    emails["email_domain"] = emails["email"].apply(lambda x: y.groups()[0] if (y := re.match(pattern, x)) else None)
    return (emails
            .groupby(by="email_domain", as_index=False, dropna=True)
            .agg(count=("email", "count"))
            .sort_values(by="email_domain", ascending=True))

emails = pd.read_excel(Path(os.getcwd()) / "data" / "3059. Find All Unique Email Domains.xlsx")
print(find_unique_email_domains(emails))
