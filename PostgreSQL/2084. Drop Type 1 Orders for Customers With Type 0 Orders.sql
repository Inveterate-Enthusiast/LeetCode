Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| customer_id | int  |
| order_type  | int  |
+-------------+------+
order_id is the column with unique values for this table.
Each row of this table indicates the ID of an order, the ID of the customer who ordered it, and the order type.
The orders could be of type 0 or type 1.


Write a solution to report all the orders based on the following criteria:

If a customer has at least one order of type 0, do not report any order of type 1 from that customer.
Otherwise, report all the orders of the customer.
Return the result table in any order.



1.
WITH added AS
    (
    SELECT *, MIN(order_type) OVER(PARTITION BY customer_id) AS our_min
    FROM Orders
    )
SELECT order_id, customer_id, order_type
FROM added
WHERE (our_min = 0 AND order_type = 0)
OR (our_min <> 0);