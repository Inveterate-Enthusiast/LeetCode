# Table: Customer
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | referee_id  | int     |
# +-------------+---------+
# In SQL, id is the primary key column for this table.
# Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

# Find the names of the customer that are not referred by the customer with id = 2.
#
# Return the result table in any order.

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer.drop(index=customer[customer["referee_id"] == 2].index, axis=0, inplace=True)
    return customer[["name"]]

def find_customer_referee1(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[(customer["referee_id"] != 2) | (customer["referee_id"].isna())][["name"]]

def find_customer_referee2(customer: pd.DataFrame) -> pd.DataFrame:
    return customer.query("(referee_id != 2) | (referee_id.isna())")[["name"]]

Customers = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "name": ["Will", "Jane", "Alex", "Bill", "Zack", "Mark"],
    "referee_id": [None, None, 2, None, 1, 2]
})

print(find_customer_referee2(Customers))

