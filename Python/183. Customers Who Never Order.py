# Table: Customers
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID and name of a customer.

# Table: Orders
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# customerId is a foreign key (reference columns) of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

# Write a solution to find all customers who never order anything.
#
# Return the result table in any order.
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders.drop_duplicates("customerId", keep="first")
    ans_df = pd.merge(
        left = customers,
        right = orders,
        left_on = "id",
        right_on = "customerId",
        how = "left",
        suffixes = ("_cus", "_or")
    )
    return ans_df[ans_df["id_or"].isna()][["name"]].rename(columns={"name": "Customers"})

def find_customers1(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers[~customers["id"].isin(orders['customerId'])][["name"]].rename(columns={"name": "Customers"})

Customers = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Joe", "Henry", "Sam", "Max"]
})

Orders = pd.DataFrame({
    "id": [1, 2],
    "customerId": [3, 1]
})

print(find_customers1(Customers, Orders))
