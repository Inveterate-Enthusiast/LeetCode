# Table Variables:
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | name          | varchar |
# | value         | int     |
# +---------------+---------+
# In SQL, name is the primary key for this table.
# This table contains the stored variables and their values.
#
#
# Table Expressions:
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | left_operand  | varchar |
# | operator      | enum    |
# | right_operand | varchar |
# +---------------+---------+
# In SQL, (left_operand, operator, right_operand) is the primary key for this table.
# This table contains a boolean expression that should be evaluated.
# operator is an enum that takes one of the values ('<', '>', '=')
# The values of left_operand and right_operand are guaranteed to be in the Variables table.
#
#
# Evaluate the boolean expressions in Expressions table.
#
# Return the result table in any order.
import pandas as pd

def eval_expression(variables: pd.DataFrame, expressions: pd.DataFrame) -> pd.DataFrame:
    _dict = dict()
    for index, row in variables.iterrows():
        _dict[row["name"]] = row["value"]

    if not expressions.empty:
        expressions["value"] = expressions.apply(lambda x: str(eval(str(_dict[x["left_operand"]]) +
                                                            str(x["operator"]*2 if x["operator"] == "=" else x["operator"]) +
                                                            str(_dict[x["right_operand"]]))).lower(),
                                                axis=1)
    else:
        expressions["value"] = None
    return expressions

