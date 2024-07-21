# Table: Orders
#
# +-----------------+----------+
# | Column Name     | Type     |
# +-----------------+----------+
# | order_number    | int      |
# | customer_number | int      |
# +-----------------+----------+
# order_number is the primary key (column with unique values) for this table.
# This table contains information about the order ID and the customer ID.

# Write a solution to find the customer_number for the customer who has placed the largest number of orders.
#
# The test cases are generated so that exactly one customer will have placed more orders than any other customer.
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    grouped = orders.groupby(
        by="customer_number",
        as_index=False
    ).size()
    if not grouped.empty:
        return grouped[grouped["size"] == max(grouped["size"])][["customer_number"]]
    else:
        return grouped[["customer_number"]]

def largest_orders1(orders: pd.DataFrame) -> pd.DataFrame:
    grouped = orders.groupby(
        by="customer_number",
        as_index=False
    ).size()
    return grouped[grouped["size"] == grouped["size"].max()][["customer_number"]]

def largest_orders2(orders: pd.DataFrame) -> pd.DataFrame:
    return orders[orders["customer_number"].isin(orders["customer_number"].mode())][["customer_number"]].drop_duplicates()

def largest_orders2(orders: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(orders["customer_number"].mode())

Orders = pd.DataFrame({
    "order_number": [1, 2, 3, 4],
    "customer_number": [1, 2, 3, 3]
})

# print(Orders.groupby(by=["customer_number"], as_index=False).size())

print(largest_orders2(Orders))

