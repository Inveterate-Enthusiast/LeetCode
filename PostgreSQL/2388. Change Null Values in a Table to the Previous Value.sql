Table: CoffeeShop

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| drink       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row in this table shows the order id and the name of the drink ordered. Some drink rows are nulls.


Write a solution to replace the null values of the drink with the name of the drink of the previous row that is not null.
It is guaranteed that the drink on the first row of the table is not null.

Return the result table in the same order as the input.


1.
WITH bool AS (
    SELECT
        *,
        (CASE WHEN drink IS NULL THEN 0 ELSE 1 END) AS bool,
        ROW_NUMBER() OVER() AS row
    FROM CoffeeShop
),
groups AS (
    SELECT
        *,
        SUM(bool) OVER(ORDER BY row ASC) AS our_group
    FROM bool
)
SELECT
    id,
    COALESCE(drink, FIRST_VALUE(drink) OVER(PARTITION BY our_group)) AS drink
FROM groups