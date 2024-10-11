# Table: Sales
#
# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | sale_id     | int   |
# | product_id  | int   |
# | user_id     | int   |
# | quantity    | int   |
# +-------------+-------+
# sale_id contains unique values.
# product_id is a foreign key (reference column) to Product table.
# Each row of this table shows the ID of the product and the quantity purchased by a user.
#
#
# Table: Product
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | product_id  | int  |
# | price       | int  |
# +-------------+------+
# product_id contains unique values.
# Each row of this table indicates the price of each product.
#
#
# Write a solution that reports for each user the product id on which the user spent the most money.
# In case the same user spent the most money on two or more products, report all of them.
#
# Return the resulting table in any order.
import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=sales,
        right=product,
        how="left",
        on="product_id"
    )
    merged["amount"] = merged["quantity"] * merged["price"]
    grouped = merged.groupby(by=["user_id", "product_id"], as_index=False).agg(amount=("amount", "sum"))
    grouped["rank"] = grouped.groupby(by="user_id", as_index=False)["amount"].rank(method="dense", ascending=False)
    return grouped.loc[grouped["rank"] == 1, ["user_id", "product_id"]]


