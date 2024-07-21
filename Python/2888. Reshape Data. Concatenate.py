# Write a solution to concatenate these two DataFrames vertically into one DataFrame.
#
# The result format is in the following example.


import pandas as pd

def concatenateTables1(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    newDataFrame = pd.merge(df1, df2, how= "outer")
    return newDataFrame

def concatenateTables2(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    newDataFrame = pd.concat([df1, df2], axis= 0, join= "outer")
    return newDataFrame

OurDataFrame1 = {
    "student_id": [1, 2, 3, 4],
    "name": ["Mason", "Ava", "Taylor", "Georgia"],
    "age": [8, 6, 15, 17]
}
OurDataFrame1 = pd.DataFrame(OurDataFrame1)
OurDataFrame2 = {
    "student_id": [5, 6],
    "name": ["Leo", "Ales"],
    "age": [7, 36]
}
OurDataFrame2 = pd.DataFrame(OurDataFrame2)

print(concatenateTables2(OurDataFrame1, OurDataFrame2))