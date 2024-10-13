Table: Salesperson

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| salesperson_id | int     |
| name           | varchar |
+----------------+---------+
salesperson_id contains unique values.
Each row in this table shows the ID of a salesperson.


Table: Customer

+----------------+------+
| Column Name    | Type |
+----------------+------+
| customer_id    | int  |
| salesperson_id | int  |
+----------------+------+
customer_id contains unique values.
salesperson_id is a foreign key (reference column) from the Salesperson table.
Each row in this table shows the ID of a customer and the ID of the salesperson.


Table: Sales

+-------------+------+
| Column Name | Type |
+-------------+------+
| sale_id     | int  |
| customer_id | int  |
| price       | int  |
+-------------+------+
sale_id contains unique values.
customer_id is a foreign key (reference column) from the Customer table.
Each row in this table shows ID of a customer and the price they paid for the sale with sale_id.


Write a solution to report the sum of prices paid by the customers of each salesperson.
If a salesperson does not have any customers, the total value should be 0.

Return the result table in any order.


1.
WITH grouped AS (
    SELECT
        customer_id,
        SUM(price) AS total
    FROM Sales
    GROUP BY customer_id
),
merged AS (
    SELECT
        main.salesperson_id,
        COALESCE(sub.total, 0) AS total
    FROM Customer AS main
    LEFT JOIN grouped AS sub
    ON sub.customer_id = main.customer_id
),
grouped_2 AS (
    SELECT
        salesperson_id,
        SUM(total) AS total
    FROM merged
    GROUP BY salesperson_id
)
SELECT
    main.salesperson_id,
    main.name,
    COALESCE(sub.total, 0) AS total
FROM Salesperson AS main
LEFT JOIN grouped_2 AS sub
ON sub.salesperson_id = main.salesperson_id;