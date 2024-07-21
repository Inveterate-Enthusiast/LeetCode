# Table: Person
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | personId    | int     |
# | lastName    | varchar |
# | firstName   | varchar |
# +-------------+---------+
# personId is the primary key (column with unique values) for this table.
# This table contains information about the ID of some persons and their first and last names.

# Table: Address
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | addressId   | int     |
# | personId    | int     |
# | city        | varchar |
# | state       | varchar |
# +-------------+---------+
# addressId is the primary key (column with unique values) for this table.
# Each row of this table contains information about the city and state of one person with ID = PersonId.

# Write a solution to report the first name, last name, city, and state of each person in the Person table.
# If the address of a personId is not present in the Address table, report null instead.
#
# Return the result table in any order.

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(
        left = person,
        right = address,
        how = "left",
        left_on = "personId",
        right_on = "personId",
        copy = True,

    )[["firstName", "lastName", "city", "state"]]

Person = pd.DataFrame({
    "personId": [1, 2],
    "lastName": ["Wang", "Alice"],
    "firstName": ["Allen", "Bob"]
})

Address = pd.DataFrame({
    "addressId": [1, 2],
    "personId": [2, 3],
    "city": ["New York City", "LeetCode"],
    "state": ["New York", "California"]
})

print(combine_two_tables(Person, Address))