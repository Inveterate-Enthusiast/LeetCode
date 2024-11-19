# Table: Transactions
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | transaction_id   | int     |
# | customer_id      | int     |
# | product_id       | int     |
# | transaction_date | date    |
# | amount           | decimal |
# +------------------+---------+
# transaction_id is the unique identifier for this table.
# Each row of this table contains information about a transaction, including the customer ID, product ID, date, and amount spent.
# Table: Products
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | category    | varchar |
# | price       | decimal |
# +-------------+---------+
# product_id is the unique identifier for this table.
# Each row of this table contains information about a product, including its category and price.
# Write a solution to analyze customer purchasing behavior. For each customer, calculate:
#
# The total amount spent.
# The number of transactions.
# The number of unique product categories purchased.
# The average amount spent.
# The most frequently purchased product category (if there is a tie, choose the one with the most recent transaction).
# A loyalty score defined as: (Number of transactions * 10) + (Total amount spent / 100).
# Round total_amount, avg_transaction_amount, and loyalty_score to 2 decimal places.
#
# Return the result table ordered by loyalty_score in descending order, then by customer_id in ascending order.
import pandas as pd

def grouping(df: pd.DataFrame) -> pd.Series:
    total_amount = (df["amount"].sum() + 1e-9).round(2)
    transaction_count = df["transaction_id"].nunique()
    unique_categories = df["category"].nunique()
    avg_transaction_amount = (df["amount"].mean() + 1e-9).round(2)
    category_grouped = df.groupby(by="category", as_index=False).agg(freq=("transaction_id", "nunique"), maxdate=("transaction_date", "max"))
    sorted_category = category_grouped.sort_values(by=["freq", "maxdate"], ascending=[False, False])
    top_category = sorted_category["category"].iloc[0]
    loyalty_score = ((transaction_count * 10) + (total_amount / 100) + 1e-9).round(2)
    return pd.Series(data=[total_amount, transaction_count, unique_categories, avg_transaction_amount, top_category, loyalty_score],
                     index=["total_amount", "transaction_count", "unique_categories", "avg_transaction_amount", "top_category", "loyalty_score"])

def analyze_customer_behavior(transactions: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        left=transactions,
        right=products,
        how="left",
        on="product_id"
    )
    if merged.empty:
        return pd.DataFrame({
            "customer_id": list(),
            "total_amount": list(),
            "transaction_count": list(),
            "unique_categories": list(),
            "avg_transaction_amount": list(),
            "top_category": list(),
            "loyalty_score": list()
        })
    grouped = merged.groupby(by="customer_id", as_index=True).apply(grouping, include_groups=False).reset_index()
    return grouped.sort_values(by=["loyalty_score", "customer_id"], ascending=[False, True])
