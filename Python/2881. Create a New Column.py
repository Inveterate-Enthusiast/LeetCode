# A company plans to provide its employees with a bonus.
#
# Write a solution to create a new column name bonus that contains the doubled values of the salary column.
#
# The result format is in the following example.

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = [i * 2 for i in employees["salary"]]
    return employees

data = [
    ["Piter", 4548],
    ["Grace", 28150],
    ["Georgia", 1103],
    ["Willow", 6593],
    ["Finn", 74576],
    ["Thomas", 24433],
]

OurEmployee = pd.DataFrame(data, columns= ["name", "salary"])
print(createBonusColumn(OurEmployee))