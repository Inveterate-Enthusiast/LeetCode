Table: SalesPerson

+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+
sales_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.

Table: Company

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
com_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a company and the city in which the company is located.

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id is the primary key (column with unique values) for this table.
com_id is a foreign key (reference column) to com_id from the Company table.
sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.

1.
WITH merged AS
(SELECT DISTINCT main.sales_id AS sales_id FROM Orders AS main JOIN (SELECT * FROM Company WHERE name = 'RED') AS sub ON main.com_id = sub.com_id)
SELECT sel.name FROM SalesPerson AS sel WHERE sel.sales_id NOT IN (SELECT sales_id FROM merged);
2.
WITH merged_1 AS
(SELECT com.com_id, com.name, ord.sales_id FROM Company AS com FULL OUTER JOIN Orders AS ord ON com.com_id = ord.com_id),
merged_2 AS
(SELECT sel.sales_id, sel.name AS sel_name, mer.com_id, mer.name AS mer_name FROM SalesPerson AS sel FULL OUTER JOIN merged_1 AS mer ON sel.sales_id = mer.sales_id),
merged_3 AS
(SELECT sel_name, ARRAY_AGG(DISTINCT mer_name) AS our_set FROM merged_2 GROUP BY sel_name)
SELECT sel_name AS name FROM merged_3 WHERE ('RED' <> ALL(our_set) OR array_length(our_set, 1) = 0 OR (array_length(our_set, 1) = 1 AND our_set[1] IS NULL)) AND sel_name IS NOT NULL;
