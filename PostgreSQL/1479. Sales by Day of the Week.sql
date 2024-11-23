Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| order_date    | date    |
| item_id       | varchar |
| quantity      | int     |
+---------------+---------+
(ordered_id, item_id) is the primary key (combination of columns with unique values) for this table.
This table contains information on the orders placed.
order_date is the date item_id was ordered by the customer with id customer_id.


Table: Items

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| item_id             | varchar |
| item_name           | varchar |
| item_category       | varchar |
+---------------------+---------+
item_id is the primary key (column with unique values) for this table.
item_name is the name of the item.
item_category is the category of the item.


You are the business owner and would like to obtain a sales report for category items and the day of the week.

Write a solution to report how many units in each category have been ordered on each day of the week.

Return the result table ordered by category.




1.
SELECT
    main.item_category AS Category,
    SUM(CASE WHEN EXTRACT(DOW FROM order_date) = 1 THEN COALESCE(sub.quantity, 0) ELSE 0 END) AS Monday,
    SUM(CASE WHEN EXTRACT(DOW FROM order_date) = 2 THEN COALESCE(sub.quantity, 0) ELSE 0 END) AS Tuesday,
    SUM(CASE WHEN EXTRACT(DOW FROM order_date) = 3 THEN COALESCE(sub.quantity, 0) ELSE 0 END) AS Wednesday,
    SUM(CASE WHEN EXTRACT(DOW FROM order_date) = 4 THEN COALESCE(sub.quantity, 0) ELSE 0 END) AS Thursday,
    SUM(CASE WHEN EXTRACT(DOW FROM order_date) = 5 THEN COALESCE(sub.quantity, 0) ELSE 0 END) AS Friday,
    SUM(CASE WHEN EXTRACT(DOW FROM order_date) = 6 THEN COALESCE(sub.quantity, 0) ELSE 0 END) AS Saturday,
    SUM(CASE WHEN EXTRACT(DOW FROM order_date) = 0 THEN COALESCE(sub.quantity, 0) ELSE 0 END) AS Sunday
FROM Items AS main

LEFT JOIN Orders AS sub
    ON sub.item_id = main.item_id

GROUP BY main.item_category
ORDER BY main.item_category ASC;