# A company intends to give its employees a pay rise.
#
# Write a solution to modify the salary column by multiplying each salary by 2.
#
# The result format is in the following example.

import pandas as pd

def modifySalaryColumn1(employees: pd.DataFrame) -> pd.DataFrame:
    for index, row in employees.iterrows():
        employees.loc[index, "salary"] *= 2
    return employees

def modifySalaryColumn2(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] *= 2
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

print(modifySalaryColumn2(OurEmployee))

string = "привет"
print(string*2)