# There are some rows having missing values in the name column.
#
# Write a solution to remove the rows with missing values.
#
# The result format is in the following example.
import pandas as pd
def dropMissingData1(students: pd.DataFrame) -> pd.DataFrame:
    OurToRemoveRows = []
    for index, row in students.iterrows():
        if row["name"] == None or len(row['name']) == 0:
            OurToRemoveRows.append(index)
    students = students.drop(OurToRemoveRows)
    return students

def dropMissingData2(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(axis= 0, how= "any", subset= "name", inplace= True)
    return students

data = [
    [1, "", "emily@example.com"],
    [2, "David", "michael@example.com"],
    [3, "Zachary", "sarah@example.com"],
    [4, None, "john@example.com"],
    [5, "Finn", "john@example.com"],
    [6, "Violet", "alice@example.com"],
]

data = pd.DataFrame(data, columns= ["customer_id", "name", "email"])

print(dropMissingData2(data))