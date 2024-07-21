# Table: Product
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | name        | varchar |
# +-------------+---------+
# product_id is the column with unique values for this table.
# This table contains the ID and the name of the product. The name consists of only lowercase English letters. No two products have the same name.
#
#
# Table: Invoice
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | invoice_id  | int  |
# | product_id  | int  |
# | rest        | int  |
# | paid        | int  |
# | canceled    | int  |
# | refunded    | int  |
# +-------------+------+
# invoice_id is the column with unique values for this table and the id of this invoice.
# product_id is the id of the product for this invoice.
# rest is the amount left to pay for this invoice.
# paid is the amount paid for this invoice.
# canceled is the amount canceled for this invoice.
# refunded is the amount refunded for this invoice.
#
#
# Write a solution that will, for all products, return each product name with the total amount due, paid, canceled, and refunded across all invoices.
#
# Return the result table ordered by product_name.
import pandas as pd

def analyze_products(product: pd.DataFrame, invoice: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=product,
        right=invoice,
        how="outer",
        on="product_id",
        copy=False
    )
    return (merged.groupby(by=["product_id", "name"], as_index=False)[["rest", "paid", "canceled", "refunded"]]
            .sum()
            .drop(columns=["product_id"])
            .sort_values(by="name", ascending=True))
