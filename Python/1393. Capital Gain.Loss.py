# Table: Stocks
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | stock_name    | varchar |
# | operation     | enum    |
# | operation_day | int     |
# | price         | int     |
# +---------------+---------+
# (stock_name, operation_day) is the primary key (combination of columns with unique values) for this table.
# The operation column is an ENUM (category) of type ('Sell', 'Buy')
# Each row of this table indicates that the stock which has stock_name had an operation on the day operation_day with the price.
# It is guaranteed that each 'Sell' operation for a stock has a corresponding 'Buy' operation in a previous day.
# It is also guaranteed that each 'Buy' operation for a stock has a corresponding 'Sell' operation in an upcoming day.
#
#
# Write a solution to report the Capital gain/loss for each stock.
#
# The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.
#
# Return the result table in any order.
import pandas as pd
from pathlib import Path
import os

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    return (stocks
            .groupby(by="stock_name", as_index=False)
            .apply(lambda x:
                            pd.Series(
                                data=(
                                        sum(x.loc[x["operation"] == "Sell", "price"])
                                        -
                                        sum(x.loc[x["operation"] == "Buy", "price"])),
                                index=["capital_gain_loss"]),
                   include_groups=False))

stocks = pd.read_excel(Path(os.getcwd()) / "data" / "1393. Capital Gain.Loss.xlsx")
print(capital_gainloss(stocks))
