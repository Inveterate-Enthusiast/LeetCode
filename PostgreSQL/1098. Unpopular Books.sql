Table: Books

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| book_id        | int     |
| name           | varchar |
| available_from | date    |
+----------------+---------+
book_id is the primary key (column with unique values) of this table.


Table: Orders

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| order_id       | int     |
| book_id        | int     |
| quantity       | int     |
| dispatch_date  | date    |
+----------------+---------+
order_id is the primary key (column with unique values) of this table.
book_id is a foreign key (reference column) to the Books table.


Write a solution to report the books that have sold less than 10 copies in the last year,
excluding books that have been available for less than one month from today. Assume today is 2019-06-23.

Return the result table in any order.

1.
WITH filtered AS
    (SELECT book_id, SUM(quantity) AS sum
    FROM Orders
    WHERE dispatch_date > ('2019-06-23'::DATE - INTERVAL '1 YEAR')
    GROUP BY book_id)
SELECT main.book_id, main.name
FROM (SELECT book_id, name
        FROM Books
        WHERE (EXTRACT(MONTH FROM (AGE('2019-06-23'::DATE, available_from))) + 12 * EXTRACT(YEAR FROM (AGE('2019-06-23'::DATE, available_from)))) > 0) AS main
LEFT JOIN
filtered AS sub
ON main.book_id = sub.book_id
WHERE COALESCE(sub.sum, 0) < 10;