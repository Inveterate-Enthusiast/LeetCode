# There are some duplicate rows in the DataFrame based on the email column.
#
# Write a solution to remove these duplicate rows and keep only the first occurrence.
#
# The result format is in the following example.

import pandas as pd

def dropDuplicateEmails1(customers: pd.DataFrame) -> pd.DataFrame:
    OurDict = {}
    DublicatedRows = []
    for index, row in customers.iterrows():
        if row["email"] in OurDict:
            DublicatedRows.append(index)
        else:
            OurDict[row["email"]] = 1
    customers = customers.drop(DublicatedRows)
    return customers

def dropDuplicateEmails2(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset="email", keep="first", inplace=True)
    return customers

data = [
    [1, "Ella", "emily@example.com"],
    [2, "David", "michael@example.com"],
    [3, "Zachary", "sarah@example.com"],
    [4, "Alice", "john@example.com"],
    [5, "Finn", "john@example.com"],
    [6, "Violet", "alice@example.com"],
]

data = pd.DataFrame(data, columns= ["customer_id", "name", "email"])
print(dropDuplicateEmails2(data))