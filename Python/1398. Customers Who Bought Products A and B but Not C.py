# Table: Customers
#
# +---------------------+---------+
# | Column Name         | Type    |
# +---------------------+---------+
# | customer_id         | int     |
# | customer_name       | varchar |
# +---------------------+---------+
# customer_id is the column with unique values for this table.
# customer_name is the name of the customer.
#
#
# Table: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | customer_id   | int     |
# | product_name  | varchar |
# +---------------+---------+
# order_id is the column with unique values for this table.
# customer_id is the id of the customer who bought the product "product_name".
#
#
# Write a solution to report the customer_id and customer_name of customers who bought products "A", "B"
# but did not buy the product "C" since we want to recommend them to purchase this product.
#
# Return the result table ordered by customer_id.
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    grouped = (orders
               .merge(right=customers, on="customer_id", how="left")
               .groupby(by=["customer_id", "customer_name"], as_index=False)
               .agg(product_set=("product_name", lambda x: set(x))))
    return (grouped
            .loc[
            ~(grouped["product_set"] >= set("C")) &
            (grouped["product_set"] >= set(["A", "B"])),
            ["customer_id", "customer_name"]
        ].sort_values(by="customer_id", ascending=True)
    )



