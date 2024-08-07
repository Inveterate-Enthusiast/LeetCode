# Table: Customers
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | customer_id   | int     |
# | customer_name | varchar |
# | email         | varchar |
# +---------------+---------+
# customer_id is the column of unique values for this table.
# Each row of this table contains the name and the email of a customer of an online shop.
#
#
# Table: Contacts
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | id      |
# | contact_name  | varchar |
# | contact_email | varchar |
# +---------------+---------+
# (user_id, contact_email) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the name and email of one contact of customer with user_id.
# This table contains information about people each customer trust. The contact may or may not exist in the Customers table.
#
#
# Table: Invoices
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | invoice_id   | int     |
# | price        | int     |
# | user_id      | int     |
# +--------------+---------+
# invoice_id is the column of unique values for this table.
# Each row of this table indicates that user_id has an invoice with invoice_id and a price.
#
#
# Write a solution to find the following for each invoice_id:
#
# customer_name: The name of the customer the invoice is related to.
# price: The price of the invoice.
# contacts_cnt: The number of contacts related to the customer.
# trusted_contacts_cnt: The number of contacts related to the customer and at the same time they are customers to the shop.
# (i.e their email exists in the Customers table.)
# Return the result table ordered by invoice_id.
import pandas as pd

def count_trusted_contacts(customers: pd.DataFrame, contacts: pd.DataFrame, invoices: pd.DataFrame) -> pd.DataFrame:
    set_customers = set(customers["email"].values)
    merged = pd.merge(
        left=customers[["customer_id", "customer_name"]].rename(columns={"customer_id": "user_id"}),
        right=contacts[["user_id", "contact_email"]],
        on="user_id",
        how="left",
        copy=False
    )
    grouped = (merged
               .groupby(by=["user_id", "customer_name"], as_index=False)
               .agg(
                    contacts_cnt=("contact_email", "nunique"),
                    trusted_contacts_cnt=("contact_email", lambda x: x[x.isin(set_customers)].nunique())))
    return pd.merge(
        left=invoices,
        right=grouped,
        on="user_id",
        how="left"
    ).sort_values(by="invoice_id", ascending=True)[["invoice_id", "customer_name", "price", "contacts_cnt", "trusted_contacts_cnt"]]

