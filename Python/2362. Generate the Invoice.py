# Table: Products
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | product_id  | int  |
# | price       | int  |
# +-------------+------+
# product_id contains unique values.
# Each row in this table shows the ID of a product and the price of one unit.
#
#
# Table: Purchases
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | invoice_id  | int  |
# | product_id  | int  |
# | quantity    | int  |
# +-------------+------+
# (invoice_id, product_id) is the primary key (combination of columns with unique values) for this table.
# Each row in this table shows the quantity ordered from one product in an invoice.
#
#
# Write a solution to show the details of the invoice with the highest price. If two or more invoices have the same price,
# return the details of the one with the smallest invoice_id.
#
# Return the result table in any order.

import pandas as pd

def generate_the_invoice(products: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=purchases,
        right=products,
        how="left",
        on="product_id"
    ).fillna(0)
    merged["price"] = merged["quantity"] * merged["price"]
    merged["sum"] = merged.groupby(by="invoice_id", as_index=False)["price"].transform("sum")
    merged.sort_values(by=["sum", "invoice_id"], ascending=[False, True], inplace=True)
    merged["rank"] = pd.factorize(merged["invoice_id"])[0] + 1
    return (merged
            .loc[merged["rank"] == 1]
            .groupby(by="product_id", as_index=False)
            .agg(quantity=("quantity", "sum"),
                 price=("price", "sum")))