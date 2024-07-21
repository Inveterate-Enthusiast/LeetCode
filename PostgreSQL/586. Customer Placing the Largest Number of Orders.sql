Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
 

Write a solution to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

1.
WITH 
sub AS 
(SELECT customer_number, COUNT(order_number) AS our_count FROM Orders GROUP BY customer_number),
max_count AS
(SELECT MAX(our_count) AS max_out_count FROM sub)
SELECT customer_number FROM sub WHERE our_count = (SELECT max_out_count FROM max_count);
2.
WITH
sub AS
(SELECT customer_number, COUNT(order_number) AS our_count FROM Orders GROUP BY customer_number)
SELECT customer_number FROM sub WHERE our_count = (SELECT MAX(our_count) FROM sub);
3.
WITH
sub AS
(SELECT customer_number, COUNT(order_number) AS our_count FROM Orders GROUP BY customer_number ORDER BY our_count DESC FETCH FIRST 1 ROW ONLY)
SELECT customer_number FROM sub;