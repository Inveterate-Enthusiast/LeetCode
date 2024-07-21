# Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.
#
# The result format is in the following example.

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    newReport = report.melt(id_vars= "product", value_vars= ["quarter_1", "quarter_2", "quarter_3", "quarter_4"], value_name= "sales", var_name= "quarter")
    return newReport

data = {
    "product": ["Umbrella", "SleepingBag"],
    "quarter_1":[417, 800],
    "quarter_2":[224, 936],
    "quarter_3":[379, 93],
    "quarter_4":[611, 875]
}

data = pd.DataFrame(data)
print(meltTable(data))