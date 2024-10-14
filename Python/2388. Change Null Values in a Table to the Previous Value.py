# Table: CoffeeShop
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | drink       | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row in this table shows the order id and the name of the drink ordered. Some drink rows are nulls.
#
#
# Write a solution to replace the null values of the drink with the name of the drink of the previous row that is not null. It is guaranteed that the drink on the first row of the table is not null.
#
# Return the result table in the same order as the input.
import pandas as pd

def change_null_values(coffee_shop: pd.DataFrame) -> pd.DataFrame:
    tempDrink = None
    for index, row in coffee_shop.iterrows():
        if not tempDrink or pd.notna(row["drink"]):
            tempDrink = row["drink"]
        else:
            coffee_shop.loc[index, "drink"] = tempDrink

    return coffee_shop

def change_null_values1(coffee_shop: pd.DataFrame) -> pd.DataFrame:
    return coffee_shop.fillna(method="ffill")

def change_null_values2(coffee_shop: pd.DataFrame) -> pd.DataFrame:
    return coffee_shop.ffill()