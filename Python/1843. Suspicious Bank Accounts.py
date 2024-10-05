# Table: Accounts
#
# +----------------+------+
# | Column Name    | Type |
# +----------------+------+
# | account_id     | int  |
# | max_income     | int  |
# +----------------+------+
# account_id is the column with unique values for this table.
# Each row contains information about the maximum monthly income for one bank account.
#
#
# Table: Transactions
#
# +----------------+----------+
# | Column Name    | Type     |
# +----------------+----------+
# | transaction_id | int      |
# | account_id     | int      |
# | type           | ENUM     |
# | amount         | int      |
# | day            | datetime |
# +----------------+----------+
# transaction_id is the column with unique values for this table.
# Each row contains information about one transaction.
# type is ENUM (category) type of ('Creditor','Debtor') where 'Creditor' means the user deposited money into their
# account and 'Debtor' means the user withdrew money from their account.
# amount is the amount of money deposited/withdrawn during the transaction.
#
#
# A bank account is suspicious if the total income exceeds the max_income for this account for two
# or more consecutive months. The total income of an account in some month is the sum of all its deposits in that month
# (i.e., transactions of the type 'Creditor').
#
# Write a solution to report the IDs of all suspicious bank accounts.
#
# Return the result table in any order.
import pandas as pd

def suspicious_bank_accounts(accounts: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["month"] = pd.to_datetime(transactions["day"]).dt.month
    grouped = transactions.loc[transactions["type"] == "Creditor"].groupby(by=["account_id", "month"], as_index=False).agg(total_sum=("amount", "sum"))
    merged = pd.merge(
        left=accounts,
        right=grouped,
        how="left",
        on="account_id"
    )
    merged["bool"] = merged["total_sum"] > merged["max_income"]
    merged.sort_values(by=["account_id", "month"], ascending=[True, True], inplace=True)
    merged["diff"] = merged.groupby(by="account_id", as_index=False)["month"].diff()
    merged["cons"] = merged.groupby(by="account_id")["bool"].transform(lambda x: x * x.shift(1).fillna(False))
    return merged.loc[(merged["cons"]) & (merged["diff"] == 1), ["account_id"]].drop_duplicates(subset="account_id", keep="first")
