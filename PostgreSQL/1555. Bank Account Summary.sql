Table: Users

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| user_id      | int     |
| user_name    | varchar |
| credit       | int     |
+--------------+---------+
user_id is the primary key (column with unique values) for this table.
Each row of this table contains the current credit information for each user.


Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trans_id      | int     |
| paid_by       | int     |
| paid_to       | int     |
| amount        | int     |
| transacted_on | date    |
+---------------+---------+
trans_id is the primary key (column with unique values) for this table.
Each row of this table contains information about the transaction in the bank.
User with id (paid_by) transfer money to user with id (paid_to).


Leetcode Bank (LCB) helps its coders in making virtual payments. Our bank records all transactions in the table Transaction,
we want to find out the current balance of all users and check whether they have breached their credit limit (If their current credit is less than 0).

Write a solution to report.

user_id,
user_name,
credit, current balance after performing transactions, and
credit_limit_breached, check credit_limit ("Yes" or "No")
Return the result table in any order.


1.
WITH merged AS
    (
    SELECT COALESCE(main.user_id, sub.user_id) AS user_id, main.income, sub.expense
    FROM (SELECT paid_to AS user_id, SUM(amount) AS income FROM Transactions GROUP BY user_id) AS main
    FULL OUTER JOIN
    (SELECT paid_by AS user_id, SUM(amount) AS expense FROM Transactions GROUP BY user_id) AS sub
    ON main.user_id = sub.user_id
    )
SELECT main.user_id, main.user_name,
    (main.credit - COALESCE(sub.expense, 0) + COALESCE(sub.income, 0)) AS credit,
    (CASE WHEN (main.credit - COALESCE(sub.expense, 0) + COALESCE(sub.income, 0)) < 0 THEN 'Yes' ELSE 'No' END) AS credit_limit_breached
FROM Users AS main
LEFT JOIN
merged AS sub
ON main.user_id = sub.user_id;