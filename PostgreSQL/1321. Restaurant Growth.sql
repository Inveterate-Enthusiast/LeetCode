Table: Customer

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+
In SQL,(customer_id, visited_on) is the primary key for this table.
This table contains data about customer transactions in a restaurant.
visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
amount is the total paid by a customer.


You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before).
average_amount should be rounded to two decimal places.

Return the result table ordered by visited_on in ascending order.

1.
WITH ranked AS
    (SELECT *,
    SUM(amount) OVER(ORDER BY visited_on ASC) AS cum_sum,
    ROW_NUMBER() OVER(ORDER BY visited_on ASC) AS our_row
    FROM Customer)
SELECT main.visited_on, (COALESCE(main.cum_sum, 0) - COALESCE(sub.cum_sum, 0)) AS amount,
ROUND(((COALESCE(main.cum_sum, 0) - COALESCE(sub.cum_sum, 0))::NUMERIC / 7), 2) AS average_amount
FROM (
    SELECT *
    FROM ranked AS main
    WHERE visited_on >= (SELECT MIN(visited_on) FROM ranked) + INTERVAL '6 DAYS'
    AND our_row = (SELECT MAX(our_row) FROM ranked AS sub WHERE sub.visited_on = main.visited_on)
) AS main
LEFT JOIN
(
    SELECT *
    FROM ranked AS main
    WHERE our_row = (SELECT MAX(our_row) FROM ranked AS sub WHERE sub.visited_on = main.visited_on)
) AS sub
ON main.visited_on = (sub.visited_on + INTERVAL '7 DAYS')



2.
WITH ranked AS
    (SELECT *,
    SUM(amount) OVER(ORDER BY visited_on ASC) AS cum_sum,
    ROW_NUMBER() OVER(ORDER BY visited_on ASC) AS our_row
    FROM Customer),
new_rank AS
    (SELECT *,
    FROM ranked AS main
    WHERE our_row = (SELECT MAX(our_row) FROM ranked AS sub WHERE sub.visited_on = main.visited_on))
SELECT main.visited_on,
(COALESCE(main.cum_sum, 0) - COALESCE(sub.cum_sum, 0)) AS amount,
ROUND((COALESCE(main.cum_sum, 0) - COALESCE(sub.cum_sum, 0))::NUMERIC / 7, 2) AS average_amount
FROM new_rank AS main
LEFT JOIN
new_rank AS sub
ON main.visited_on = (sub.visited_on + INTERVAL '7 DAYS')
WHERE main.visited_on >= (SELECT visited_on FROM ranked WHERE our_row = 1) + INTERVAL '6 DAYS';