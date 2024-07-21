# Table: Products
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | store       | enum    |
# | price       | int     |
# +-------------+---------+
# In SQL, (product_id, store) is the primary key for this table.
# store is a category of type ('store1', 'store2', 'store3') where each represents the store this product is available at.
# price is the price of the product at this store.
#
#
# Find the price of each product in each store.
#
# Return the result table in any order.
import pandas as pd

def grouping(df: pd.DataFrame) -> pd.Series:
    ans = pd.Series()
    ans["store1"] = x if (x := df.loc[df["store"] == "store1"]["price"].sum()) else pd.NA
    ans["store2"] = x if (x := df.loc[df["store"] == "store2"]["price"].sum()) else pd.NA
    ans["store3"] = x if (x := df.loc[df["store"] == "store3"]["price"].sum()) else pd.NA
    return ans

def products_price(products: pd.DataFrame) -> pd.DataFrame:
    return (products
            .groupby(by="product_id", as_index=True)
            .apply(grouping, include_groups=False)
            .reset_index())


def products_price1(products: pd.DataFrame) -> pd.DataFrame:
    return products.pivot(
        index="product_id",
        columns="store",
        values="price",
    ).reset_index()